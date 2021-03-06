//
//  keldysh_gas.hpp
//
//  Originally created by Patrick Anderson.
//  Modified by Samuel Senior on 10/03/2017.
//  "keldysh_gas" contains the medium response model.
//

#include "keldysh_gas.hpp"
#include "physics_textbook.hpp"
#include "grid_tw.hpp"
#include <mkl.h>
#include "Eigen/Dense"
#include "maths_textbook.hpp"
#include <cmath>

#include "IO.hpp" // Remove this when the dipole is done properly
#include <iostream>

using namespace Eigen;

//------------------------------------------------------------------------------------------------//
//  Class implementation
//------------------------------------------------------------------------------------------------//
/*! Constructor */
keldysh_gas::keldysh_gas(double press_, grid_tw& tw_, DFTI_DESCRIPTOR_HANDLE& ft_, maths_textbook& maths_) :
    maths(maths_), tw(tw_), ft(ft_) {

    atom_density_max = press_ * 1.0e5 / (physics.k_B * 300.0);  // [atoms/m^3]
    z_max = 0.07;
    inlet_1 = 0.02;
    inlet_2 = z_max - 0.02;
    transitionLength = 0.001;

    // Ionization parameters, argon
    U = 15.76;  // [eV]
    C_kl = 0.95;
    n_star = 0.93;
    kappa = std::sqrt(U / 13.60);
}

double keldysh_gas::atom_density(double z) {//, double inlet_1, double inlet_2, double transitionLength) {
    if (z >= inlet_1 && z <= inlet_2) {
        // Constant max value
        return atom_density_max;
    } else if (z < inlet_1 - transitionLength) {
        // Ramp function up to 80%
        return atom_density_max*(z/(inlet_1 - transitionLength)) * 0.8;
    } else if (z >= inlet_1 - transitionLength && z < inlet_1) {
        // Step up from 80% to 100%
        return atom_density_max * (0.8 + 0.2*(z - (inlet_1 - transitionLength)) / (transitionLength));
    } else if (z > inlet_2 && z <= inlet_2 + transitionLength) {
        // Step down from 100% to 80%
        return atom_density_max * (1 - ((z - inlet_2)/(transitionLength)) * 0.2);
    } else if (z > inlet_2 + transitionLength && z <= z_max) {
        // Ramp down from 80% to 0%
        return atom_density_max * (1 - (z - (inlet_2 + transitionLength)) / (z_max - (inlet_2 + transitionLength))) * 0.8;
    } else {
        //std::cout << "keldysh_gas::atom_density(): Warning, z position out of range" << std::endl;
        return 0.0;
    }
}

//------------------------------------------------------------------------------------------------//
/*! Evaluate nonlinear polarization for active frequencies */
ArrayXcd keldysh_gas::nl_polarization(ArrayXd E_t_) {

    // Weak, zeros
    ArrayXcd output_zeros = ArrayXcd::Zero(tw.n_t);  // Original, returns zeros so no nonlinear polarisation
/*
    ArrayXd W_t = ionization_rate(E_t_);
    ArrayXd rho_t = electron_density(W_t);

    // 'Macroscopic aspects of attosecond pulse generation' says P_NL given by FT{N_A * X} (N_A being density of neutral atoms)
    //ArrayXd density_neutral_atoms = atom_density - rho_t;//atom_density * (maths.cumtrapz(tw.t, W_t)).exp();

    //Patrick's thesis says P_NL given by X * q_at * E_at * rho_0(0)
    ArrayXd temp_1 = ArrayXd::Zero(tw.n_t);
    ArrayXcd output = ArrayXcd::Zero(tw.n_t);

    // Get dipole moment - currently just assuming for the nearest plane to the centre of the capillary (the .col(0))
    ArrayXd dipole_slice = dipole.get_moment().col(0);

    int step_size = 2621440 / tw.n_t;
    for (int i = 0; i < tw.n_t; i++) {
        if (tw.t(i) > -40.0E-15 || tw.t(i) < 40.0E-15) {
            temp_1(i) = dipole_slice(i) * 2.0 * atom_density * sqrt(1 - rho_t(i)/atom_density);
        }

        if (std::isnan(temp_1(i)) == true) temp_1(i) = 0;
    }

    output = temp_1.cast<std::complex<double> >();
    DftiComputeForward(ft, output.data());

    ArrayXcd E_w = E_t_.cast<std::complex<double> >();
    DftiComputeForward(ft, E_w.data());


    ArrayXcd out = output.segment(tw.w_active_min_index, tw.n_active);// - physics.eps_0 * (sellmeier.square() - 1.0)*(E_w).segment(tw.w_active_min_index, tw.n_active);

    //}std::cout << "E_w: " << E_w.real().maxCoeff() << ", out: " << out.real().maxCoeff() << ", dipole: " << dipole.maxCoeff() << ", dipole_slice: Max: " << dipole_slice.real().maxCoeff() << ", Min: " << dipole_slice.real().minCoeff() << std::endl;
    
//std::cout << "NLP: tw.w_active_min_index: " << tw.w_active_min_index << ", tw.n_active: " << tw.n_active << std::endl;
    //return temp_1;
    //return output;
    //return out;
*/
    return((output_zeros).segment(tw.w_active_min_index, tw.n_active));
}

//------------------------------------------------------------------------------------------------//
/*! Calulate ionization rate (Popov, 2004) */
ArrayXd keldysh_gas::ionization_rate(ArrayXd E_t_) {

    ArrayXd F_t = (E_t_ / (std::pow(kappa, 3.0) * physics.E_at)).abs();
    ArrayXd output = physics.w_at * std::pow(kappa, 2.0) * std::sqrt(3.0 / maths.pi) *
                     std::pow(C_kl, 2.0) * std::pow(2.0, 2.0 * n_star) * F_t.pow(1.5 - (2.0 * n_star)) *
                     (-2.0 / (3.0 * F_t)).exp();
    for (int ii = 0; ii < tw.n_t; ii++)     // Remove NaN
        if (std::isnan(output(ii)) == true) output(ii) = 0;

    return(output);
}

//------------------------------------------------------------------------------------------------//
/*! Calculate free electron density (solve rate equations) */
ArrayXd keldysh_gas::electron_density(ArrayXd W_t_, double z) {

    ArrayXd output =  atom_density(z) * (1.0 - (-maths.cumtrapz(tw.t, W_t_)).exp());

    return(output);
}

//------------------------------------------------------------------------------------------------//
/*! Evaluate Current density for active frequencies */
ArrayXcd keldysh_gas::current_density(ArrayXd E_t_, double z) {

    // Prerequisites
    ArrayXd W_t = ionization_rate(E_t_);
    ArrayXd rho_t = electron_density(W_t, z);

    // Eliminate derivatives in governing equation by FT
    ArrayXcd B = (-std::pow(physics.q_at, 2.0) * rho_t * E_t_ / physics.m_at).
                 cast<std::complex<double> >();
    ArrayXd temp_1 = rho_t * W_t * physics.q_at * U * E_t_ / E_t_.abs2();
    for (int ii = 0; ii < tw.n_t; ii++)     // Remove NaN
        if (std::isnan(temp_1(ii)) == true) temp_1(ii) = 0;
    ArrayXcd C = temp_1.cast<std::complex<double> >();
    DftiComputeForward(ft, B.data()); DftiComputeForward(ft, C.data());

    // Retain active components
    ArrayXcd output = (B.segment(tw.w_active_min_index, tw.n_active) /
                       (std::complex<double>(0.0, -1.0) * tw.w_active)) -
                      (physics.eps_0 * physics.c *
                       C.segment(tw.w_active_min_index, tw.n_active));
    return(output);
}
