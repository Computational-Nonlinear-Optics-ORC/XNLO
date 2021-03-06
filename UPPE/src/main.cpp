//
//  main.cpp
//
//  Originally created by Patrick Anderson.
//  Modified by Samuel Senior on 10/03/2017.
//  Test enviroment for UPPE codes.
//

#include <mpi.h>
#include "maths_textbook.hpp"
#include "physics_textbook.hpp"
#include <mkl.h>
#include "DHT.hpp"
#include "grid_rkr.hpp"
#include "grid_tw.hpp"
#include "laser_pulse.hpp"
#include "capillary_fibre.hpp"
#include "keldysh_gas.hpp"
#include "Eigen/Dense"
#include "IO.hpp"

#include "config_settings.hpp"

#include <iostream>
#include <string>

#include "../../XNLO/lib/XNLO.hpp"

using namespace Eigen;

/*!
Originally created by Patrick Anderson.
Modified by Samuel Senior on 10/03/2017.
Test enviroment for UPPE codes.
*/
int main(int argc, char** argv){

    // Get config file path passed in from command line with "-cf" flag
    std::string args[argc];
    std::string config_file_path;
    std::string config_XNLO_file_path = "../configFiles/config_XNLO.txt";
    for (int i = 0; i < argc; i++) {
      args[i] = argv[i];
    }
    for (int i = 0; i < argc; i++) {
      if (args[i] == "-cf") {
        config_file_path = argv[i+1];
      }
    }

    // MPI
    int this_process;
    int total_processes;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &total_processes);
    MPI_Comm_rank(MPI_COMM_WORLD, &this_process);

    if (this_process == 0) {
        std::cout << "-------------------------------------------------------------------------------\n";
        std::cout << "                                  UPPE\n";
        std::cout << "-------------------------------------------------------------------------------\n";
    }

    //if (this_process == 0) {

    //--------------------------------------------------------------------------------------------//
    // 1. Program input
    //--------------------------------------------------------------------------------------------//

    // Input Settings and Parameters
    Config_Settings config;
    if(this_process == 0 && config_file_path.empty()) {
      std::cout << "Using default config file path " << config.path_config_file() << std::endl;
    } else {
        config.path_config_file_set(config_file_path);
        config.path_config_file_description_set("(std::string) Passed in by '-cf' argument");
        if (this_process == 0) {
            std::cout << "Using config file path " << config.path_config_file() << std::endl;
        }
    }
    config.read_in(config.path_config_file(), false);
    config.check_paths(false);
    if (total_processes > 1) {
        config.n_m_set(total_processes-1);
        config.n_r_set(total_processes-1);
    }
    if (this_process == 0) {
        config.print();
    }

    Config_Settings config_XNLO;
    if (total_processes > 1) {
        if(this_process == 0 && config_XNLO_file_path.empty()) {
          std::cout << "Using default config file path " << config_XNLO.path_config_file() << std::endl;
        } else {
            config_XNLO.path_config_file_set(config_XNLO_file_path);
            config_XNLO.path_config_file_description_set("(std::string) Passed in by '-cf' argument");
            if (this_process == 0) {
                std::cout << "Using config file path " << config_XNLO.path_config_file() << std::endl;
            }
        }
        config_XNLO.read_in(config_XNLO.path_config_file(), false);
        config_XNLO.check_paths(false);
        if (this_process == 0) {
            config_XNLO.print();
        }
    }

    //--------------------------------------------------------------------------------------------//
    // 2. Constructors
    //--------------------------------------------------------------------------------------------//

    // General
    maths_textbook maths(config.path_input_j0());
    physics_textbook physics;

    MKL_LONG dimensions = 1;
    MKL_LONG length = config.n_t();
    double scale = 1.0 / config.n_t();
    DFTI_DESCRIPTOR_HANDLE ft;
    DftiCreateDescriptor(&ft, DFTI_DOUBLE, DFTI_COMPLEX, dimensions, length);
    DftiSetValue(ft, DFTI_BACKWARD_SCALE, scale);
    DftiCommitDescriptor(ft);

    DHT ht(config.n_r(), maths);

    // Grids
    grid_rkr rkr(config.n_r(), config.R(), config.n_m(), maths);
    grid_tw tw_driving(config.n_t(), config.T(), config.w_active_min(), config.w_active_max(), maths);
    //grid_tw tw_hhg(80000, config.T(), 1.88e16, 1.88e17, maths);

    // Physical
    laser_pulse laser_driving(config.p_av(), config.rep(), config.fwhm(), config.l_0(), config.ceo(), config.waist(), tw_driving, rkr, ft, ht, maths);
    //laser_pulse laser_hhg(0.0, config.rep(), config.fwhm(), config.l_0(), config.ceo(), config.waist(), tw_hhg, rkr, ft, ht, maths); //Make it a zero field - possibly with contructor overloading
    
    capillary_fibre capillary_driving(config.Z(), rkr, tw_driving, physics, maths);
    //capillary_fibre capillary_hhg(config.Z(), rkr, tw_hhg, physics, maths);
    
    //Dipole_moment dipole;

    keldysh_gas gas_driving(config.press(), tw_driving, ft, maths);
    //keldysh_gas gas_hhg(config.press(), tw_hhg, ft, maths, dipole);

    //--------------------------------------------------------------------------------------------//
    // 3. Propagation
    //--------------------------------------------------------------------------------------------//
    // Main loop
    double dz_driving = capillary_driving.Z / config.n_z();
    //double dz_hhg = capillary_hhg.Z / config.n_z();

    if (this_process == 0) {
        config.print(config.path_config_log());

        std::cout << "-------------------------------------------------------------------------------\n";
        std::cout << "Main Program:\n";
        std::cout << "-------------------------------------------------------------------------------\n";

        std::cout << "Laser p_pk: " << laser_driving.p_pk << std::endl;
        std::cout << "Laser E_pk: " << laser_driving.E_pk << std::endl;
    }
    
    IO file_prop_step;

    std::string ionisation_rate_test = "ionisation_rate_test.bin";

    //Fix this at some point
    ArrayXXd dipole = ArrayXXd::Zero(config_XNLO.n_t(), config.n_r());
    ArrayXXd w = ArrayXXd::Zero(config_XNLO.n_t(), config.n_r());
    ArrayXXd E = ArrayXXd::Zero(config_XNLO.n_t(), config.n_r());
    XNLO::Result tmp;// = ArrayXXd::Zero(config_XNLO.N_t(), config.n_r());
    //ArrayXd neutral_atoms = ArrayXd::Zero(config.n_r());
    ArrayXXd neutral_atoms = ArrayXXd::Zero(config.n_t(), config.n_r());

    ArrayXXcd A_w_active;

    MPI_Barrier(MPI_COMM_WORLD);

        for (int ii = 1; ii < config.n_z() + 1; ii++) {
            if (this_process == 0) {
                std::cout << "Propagation step: " << ii << std::endl;
                laser_driving.propagate(dz_driving, capillary_driving, gas_driving);
                //Put a cout here
                //std::cout << std::endl << "---Foo_1---" << std::endl;

                // Driving pulse:
                config.step_path(ii);
                file_prop_step.overwrite(config.path_A_w_R(), false);
                file_prop_step.write_header(config.path_A_w_R(), tw_driving.n_active, rkr.n_m, false);
                file_prop_step.write_double(config.path_A_w_R(), laser_driving.A_w_active.real(), tw_driving.n_active, rkr.n_m, false);
                
                file_prop_step.overwrite(config.path_A_w_I(), false);
                file_prop_step.write_header(config.path_A_w_I(), tw_driving.n_active, rkr.n_m, false);
                file_prop_step.write_double(config.path_A_w_I(), laser_driving.A_w_active.imag(), tw_driving.n_active, rkr.n_m, false);
                
                file_prop_step.overwrite(config.path_w_active(), false);
                file_prop_step.write_header(config.path_w_active(), tw_driving.n_active, 1, false);
                file_prop_step.write_double(config.path_w_active(), tw_driving.w_active, tw_driving.n_active, 1, false);

                file_prop_step.overwrite(config.path_electron_density(), false);
                file_prop_step.write_header(config.path_electron_density(), tw_driving.n_t, rkr.n_m, false);
                file_prop_step.write_double(config.path_electron_density(), laser_driving.electron_density, tw_driving.n_t, rkr.n_m, false);
            
            //and also cout here
                //std::cout << std::endl << "---Foo_2---" << std::endl;

                // Make a function to format the A_w_active to turn it into the required E field
                // Or can do that within XNLO::XNLO, but all n_r/n_m at once would probably be
                // a slightly faster operation

                A_w_active = laser_driving.A_w_active;

                if (total_processes > 1) {
                    // Send
                    for (int j = 1; j < total_processes; j++) {
                        //std::cout << std::endl << "---Foo_2ai---" << std::endl;
                        MPI_Send(laser_driving.A_w_active.real().data(),
                                 1242 * rkr.n_r, MPI_DOUBLE, j, j, MPI_COMM_WORLD);
                        //std::cout << std::endl << "---Foo_2aii---" << std::endl;
                    }
                }
                //std::cout << std::endl << "---Foo_2b---" << std::endl;
            } else {
                // Receive
                //std::cout << std::endl << "---Foo_2c--- rank " << this_process << std::endl;
                A_w_active = ArrayXXd::Zero(1242, rkr.n_r);
                MPI_Recv(A_w_active.real().data(), 1242 * rkr.n_r, MPI_DOUBLE, 0, this_process, MPI_COMM_WORLD, &status);

                //std::cout << "Rank " << this_process << " recieved from rank 0" << std::endl;
                //std::cout << "-=-=-=-=-= rank: " << this_process << " status: " << status.MPI_SOURCE << " " << status.MPI_TAG << std::endl; 
            }

            //std::cout << std::endl << "---Foo_3---" << std::endl;

            // Put XNLO here
            // Either use MPI to collect up the results here or do it within XNLO::XNLO
            //    But XNLO already collects them up, just rather than outputting them you
            //    can return them in the return statement
            // Also double check the equation for this, there's an FFT involved at some point iirc
            //MPI_Barrier(MPI_COMM_WORLD);
            //std::cout << std::endl << "---Foo_4---" << std::endl;

            // Needs an MPI Send and Recv to collect up the acceleration from all processes
            // So don't want XNLO::XNLO to do the collecting itself but rather the logic in here to instead
            //    So Rank 0 holds all the information
            //    Ranks !0 have a block sent to them
            //    They do work and return the result
            //    So basically how the main of XNLO does it but split up between here and XNLO::XNLO
            //        So here manages splitting up the work, does the MPI_Send
            //        XNLO::XNLO has the MPI_Resvs and send back the results with the MPI_Send

            // Need rank 0 to send laser_driving.A_w_active to the other ranks as they done
            // calculate it

            if (total_processes > 1) {
                tmp = XNLO::XNLO(A_w_active, tw_driving.w_active);
            }

std::cout << "---Rank: " << this_process << std::endl;
std::cout << "    neutral_atoms.rows(): " << neutral_atoms.rows() << ", neutral_atoms.cols(): " << neutral_atoms.cols() << std::endl;
std::cout << "    laser_driving.electron_density.rows(): " << laser_driving.electron_density.rows() << ", laser_driving.electron_density.cols(): " << laser_driving.electron_density.cols() << std::endl;
            if (this_process == 0 && total_processes > 1) {
                // Do we just take the electron density at the last time step or at all of them?
                for (int j = 0; j < rkr.n_r; j++) {
                    for (int i = 0; i < config.n_t(); i++) {
                        neutral_atoms.row(i).col(j) = (laser_driving.atom_density_max - laser_driving.electron_density.row(i).col(j));
                    }
                }

                ArrayXXcd hhg;
                double w_active_min_HHG = 1.2566371e+16;
                double w_active_max_HHG = 3.1415927e+17;
                int n_active_HHG = 0;
                ArrayXd w_active_HHG;
                w = tmp.w;
                int w_active_min_index_HHG = 0;
                while (w(w_active_min_index_HHG) < w_active_min_HHG)
                    w_active_min_index_HHG++;
                int count = 0;
                while (w(count) < w_active_max_HHG) {
                    count++;
                }

                n_active_HHG = count - w_active_min_index_HHG;
                w_active_HHG = w.col(0).segment(w_active_min_index_HHG, n_active_HHG);
                E = tmp.E;

                //neutral_atoms = (laser_driving.atom_density_max - laser_driving.electron_density);
                //std::cout << "atom_density_max: " << laser_driving.atom_density_max << ", electron_density: " << laser_driving.electron_density.row(laser_driving.electron_density.rows()-1) << std::endl;
                //std::cout << "Neutral atoms: " << neutral_atoms << std::endl;
                std::cout << "dipole.rows(): " << dipole.rows() << ", dipole.cols(): " << dipole.cols() << std::endl;
                std::cout << "tmp.acceleration.rows(): " << tmp.acceleration.rows() << ", tmp.acceleration.cols(): " << tmp.acceleration.cols() << std::endl;
                std::cout << "neutral_atoms.rows(): " << neutral_atoms.rows() << ", neutral_atoms.cols(): " << neutral_atoms.cols() << std::endl;
                std::cout << "w.rows(): " << w.rows() << ", w.cols(): " << w.cols() << std::endl;
                std::cout << "w.row(0): " << w.row(0) << ", w.row(1000): " << w.row(1000) << std::endl;
                std::cout << neutral_atoms.row(0).col(0) << std::endl;

                MKL_LONG dimensions_HHG = 1;
                MKL_LONG length_HHG = config_XNLO.n_t();
                double scale_HHG = 1.0 / config_XNLO.n_t();
                DFTI_DESCRIPTOR_HANDLE ft_HHG;
                DftiCreateDescriptor(&ft_HHG, DFTI_DOUBLE, DFTI_COMPLEX, dimensions_HHG, length_HHG);
                DftiSetValue(ft_HHG, DFTI_BACKWARD_SCALE, scale_HHG);
                DftiCommitDescriptor(ft_HHG);

                ArrayXd temp_linSpace = ArrayXd::LinSpaced(config_XNLO.n_t(), -500.0e-15, 500.0e-15);
                ArrayXd window = (1 - ((0.5 * maths.pi * temp_linSpace / 500e-15).sin()).pow(50));
                dipole = tmp.acceleration;
                for (int j = 0; j < rkr.n_r; j++) {
                    for (int i = 0; i < config_XNLO.n_t(); i++) {
                        dipole.row(i).col(j) *= neutral_atoms.row(j).col(0) * window.row(i);// / (w.row(i)).pow(2);
                    }
                }
                // Apply forward spectral transform
                ArrayXXcd temp_1 = dipole.cast<std::complex<double> >();
                for (int ii = 0; ii < rkr.n_r; ii++)
                    DftiComputeForward(ft_HHG, temp_1.col(ii).data());
                //or (int j = 0; j < rkr.n_r; j++) {
                //    for (int i = 0; i < config_XNLO.n_t(); i++) {
                //        temp_1.row(i).col(j) /= (w.row(i)).pow(2);
                //    }
                //}
                
                ArrayXXcd temp_2 = temp_1;
                for (int ii = 0; ii < config_XNLO.n_t(); ii++)
                    temp_2.row(ii) = ht.forward(temp_2.row(ii));
                hhg = temp_2.block(0, 0, n_active_HHG, rkr.n_m);
                for (int j = 0; j < rkr.n_r; j++) {
                    for (int i = 0; i < n_active_HHG; i++) {
                        hhg.row(i).col(j) /= (w_active_HHG.row(i)).pow(2);
                    }
                }
                //dipole = tmp.acceleration * (laser_driving.atom_density_max - laser_driving.electron_density.row(laser_driving.electron_density.rows()-1));

                file_prop_step.overwrite(config.path_HHG_R(), false);
                file_prop_step.write_header(config.path_HHG_R(), n_active_HHG, rkr.n_m, false);
                file_prop_step.write_double(config.path_HHG_R(), hhg.real(), n_active_HHG, rkr.n_m, false);

                file_prop_step.overwrite(config.path_HHG_I(), false);
                file_prop_step.write_header(config.path_HHG_I(), n_active_HHG, rkr.n_m, false);
                file_prop_step.write_double(config.path_HHG_I(), hhg.imag(), n_active_HHG, rkr.n_m, false);

                file_prop_step.overwrite(config.path_HHG_w(), false);
                file_prop_step.write_header(config.path_HHG_w(), w_active_HHG.rows(), w_active_HHG.cols(), false);
                file_prop_step.write_double(config.path_HHG_w(), w_active_HHG, w_active_HHG.rows(), w_active_HHG.cols(), false);

                file_prop_step.overwrite(config.path_HHG_E(), false);
                file_prop_step.write_header(config.path_HHG_E(), E.rows(), E.cols(), false);
                file_prop_step.write_double(config.path_HHG_E(), E, E.rows(), E.cols(), false);
            }
        }
        std::cout << "-------------------------------------------------------------------------------\n";

        if (this_process == 0) {
            // Output
            IO file;

            file.overwrite(config.path_A_w_R());
            file.write_header(config.path_A_w_R(), tw_driving.n_active, rkr.n_m);
            file.write_double(config.path_A_w_R(), laser_driving.A_w_active.real(), tw_driving.n_active, rkr.n_m);
            
            file.overwrite(config.path_A_w_I());
            file.write_header(config.path_A_w_I(), tw_driving.n_active, rkr.n_m);
            file.write_double(config.path_A_w_I(), laser_driving.A_w_active.imag(), tw_driving.n_active, rkr.n_m);
            
            file.overwrite(config.path_w_active());
            file.write_header(config.path_w_active(), tw_driving.n_active, 1);
            file.write_double(config.path_w_active(), tw_driving.w_active, tw_driving.n_active, 1);
        }

        // Clean up
        DftiFreeDescriptor(&ft);
        MPI_Finalize();

        std::cout << "\n-------------------------------------------------------------------------------\n";
        std::cout << "UPPE successfully ran!\n";
        std::cout << "-------------------------------------------------------------------------------\n";
}
