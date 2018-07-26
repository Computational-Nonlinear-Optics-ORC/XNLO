from XNLOPostprocessing import XNLO
import numpy as np
from matplotlib import pyplot as plt

def ourLaser_50fs():

    dir = "../../Results/XNLO/ParameterScans/data/800nm_ourLaser/"
    fwhm = "50fs/"
    acceleration = ()
    w = ()
    E = ()
    max_file_name = 24

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()

    wavelength = 800e-9
    rep_rate = 1000
    pulse_length = 50.0e-15
    radius = 48.0e-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break


    simulation_parameters = {'lamda':lamda,
                             'P_av':(0.1, 0.2, 0.3, 0.4, 0.5,
                                     0.6, 0.7, 0.8, 0.9, 1.0,
                                     1.1, 1.2, 1.3, 1.4, 1.5,
                                     1.6, 1.7, 1.8, 1.9, 2.0,
                                     2.1, 2.2, 2.3, 2.4, 2.5),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':75.0E-6,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/800nm_ourLaser/50fs/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 45),
                             reverse_y=True,
                             window=1.0e-6,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def ourLaser_35fs():
    dir = "../../Results/XNLO/ParameterScans/data/800nm_ourLaser/"
    fwhm = "35fs/"
    acceleration = ()
    w = ()
    E = ()
    max_file_name = 29

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()
    wavelength = 800e-9
    rep_rate = 1000
    pulse_length = 35.0e-15
    radius = 48.0e-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break

    simulation_parameters = {'lamda':lamda,
                             'P_av':(0.1, 0.2, 0.3, 0.4, 0.5,
                                     0.6, 0.7, 0.8, 0.9, 1.0,
                                     1.1, 1.2, 1.3, 1.4, 1.5,
                                     1.6, 1.7, 1.8, 1.9, 2.0,
                                     2.1, 2.2, 2.3, 2.4, 2.5,
                                     2.6, 2.7, 2.8, 2.9, 3.0),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':75.0E-6,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/800nm_ourLaser/35fs/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 45),
                             reverse_y=True,
                             window=1.0e-6,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def oldRALLaser_40fs():
    dir = "../../Results/XNLO/ParameterScans/data/800nm_oldRALLaser/"
    fwhm = "40fs/"
    acceleration = ()
    w = ()
    E = ()
    max_file_name = 19

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()
    wavelength = 800e-9
    rep_rate = 1000
    pulse_length = 40.0e-15
    radius = 48.0e-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break

    simulation_parameters = {'lamda':lamda,
                             'P_av':(0.4, 0.8, 1.2, 1.6, 2.0,
                                     2.4, 2.8, 3.2, 3.6, 4.0,
                                     4.4, 4.8, 5.2, 5.6, 6.0,
                                     6.4, 6.8, 7.2, 7.6, 8.0),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':75.0E-6,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/800nm_oldRALLaser/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 45),
                             reverse_y=True,
                             window=1.0e-6,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def RALBlueLightSource():
    dir = "../../Results/XNLO/ParameterScans/data/400nm_RALBlueLightSource/"
    fwhm = "30fs/"
    acceleration = ()
    w = ()
    E = ()
    max_file_name = 37

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()
    wavelength = 400e-9
    rep_rate = 1000
    pulse_length = 30.0e-15
    radius = 48.0e-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break

    simulation_parameters = {'lamda':lamda,
                             'P_av':(0.2, 0.3, 0.4, 0.5, 0.6,
                                     0.7, 0.8, 0.9, 1.0, 1.1,
                                     1.2, 1.3, 1.4, 1.5, 1.6,
                                     1.7, 1.8, 1.9, 2.0, 2.1,
                                     2.2,      2.4, 2.5, 2.6,
                                     2.7, 2.8, 2.9, 3.0, 3.1,
                                     3.2, 3.3, 3.4, 3.5, 3.6,
                                     3.7, 3.8, 3.9, 4.0),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':75.0E-6,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/400nm_RALBlueLightSource/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 45),
                             reverse_y=True,
                             window=1.0e-6,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def newRALLaser():
    dir = "../../Results/XNLO/ParameterScans/data/1700nm_newRALLaser/"
    fwhm = "50fs/"
    acceleration = ()
    w = ()
    E = ()
    max_file_name = 16

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()

    wavelength = 1700e-9
    rep_rate = 100000
    pulse_length = 50.0e-15
    radius = 48.0e-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break


    simulation_parameters = {'lamda':lamda,
                             'P_av':(1, 2, 3, 4, 5,
                                     6, 7, 8, 9, 10,
                                     11, 12, 13, 14, 15,
                                     16, 17),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':75.0E-6,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/1700nm_newRALLaser/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 35),
                             reverse_y=True,
                             window=1.0e-5,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def newRALLaser_smallerCapillary():
    dir = "../../Results/XNLO/ParameterScans/data/smallerCoreFibre/1700nm_newRALLaser/"
    fwhm = "50fs/"
    acceleration = ()
    w = ()
    E = ()
    max_file_name = 16

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()

    wavelength = 1700e-9
    rep_rate = 100000
    pulse_length = 50.0e-15
    radius = 22.4e-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break


    simulation_parameters = {'lamda':lamda,
                             'P_av':(1, 2, 3, 4, 5,
                                     6, 7, 8, 9, 10,
                                     11, 12, 13, 14, 15,
                                     16, 17),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':35.0E-6,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/1700nm_newRALLaser_smallerCoreFibre/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 35),
                             reverse_y=True,
                             window=1.0e-5,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def Pharos():
    dir = "../../Results/XNLO/ParameterScans/data/1030nm_Pharos_RussellsLaser/"
    fwhm = "280fs/"

    acceleration = ()
    w = ()
    E = ()
    max_file_name = 19

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()

    wavelength = 1030e-9
    rep_rate = 200000
    pulse_length = 280.0e-15
    radius = 48.0e-6
    capillary_radius = 75.0E-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break


    simulation_parameters = {'lamda':lamda,
                             'P_av': (2, 4, 6, 8, 10,
                                      12, 14, 16, 18, 20,
                                      22, 24, 26, 28, 30,
                                      32, 34, 36, 38, 40),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':capillary_radius,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/1030nm_Pharos/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 20),
                             reverse_y=True,
                             window=1.0e-6,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

def Pharos_smallerCoreFibre():
    dir = "../../Results/XNLO/ParameterScans/data/smallerCoreFibre/1030nm_Pharos_RussellsLaser/"
    fwhm = "280fs/"

    acceleration = ()
    w = ()
    E = ()
    max_file_name = 19

    lamda = ()
    RR = ()
    FWHM = ()
    spot_radius = ()

    wavelength = 1030e-9
    rep_rate = 200000
    pulse_length = 280.0e-15
    radius = 22.4e-6
    capillary_radius = 35.0E-6

    for j in range(10):
        for i in range(10):
            if j*10 + i <= max_file_name:
                acceleration = acceleration + (dir+fwhm+"0"+str(j)+str(i)+"_dipole.bin",)
                w = w + (dir+fwhm+"0"+str(j)+str(i)+"_w.bin",)
                E = E + (dir+fwhm+"0"+str(j)+str(i)+"_E.bin",)
                
                lamda = lamda + (wavelength, )
                RR = RR + (rep_rate, )
                FWHM = FWHM + (pulse_length, )
                spot_radius = spot_radius + (radius, )
            if j*10 + i > max_file_name:
                break


    simulation_parameters = {'lamda':lamda,
                             'P_av': (2, 4, 6, 8, 10,
                                      12, 14, 16, 18, 20,
                                      22, 24, 26, 28, 30,
                                      32, 34, 36, 38, 40),
                             'RR':RR,
                             'FWHM':FWHM,
                             'spot_radius':spot_radius,
                             'ROC':np.finfo(np.float64).max,
                             'CEO':0.0,
                             'radius':capillary_radius,
                             'x_min':-350*5.292E-11,
                             'x_max':350*5.292E-11}

    files = {"acceleration":acceleration,
             "w":w,
             "E":E}

    save_path = '../../Results/XNLO/ParameterScans/variedPower_FixedFWHM/1030nm_Pharos_smallerCoreFibre/'
    fname = 'combinedPowerSpectrum_energy'

    Test = XNLO(files=files, simulation_parameters=simulation_parameters)
    Test.plot.spectrum_power(energy_range=(0, 20),
                             reverse_y=True,
                             window=1.0e-6,
                             #vmin=1.0e-40,
                             normalise=False,
                             plot_against='energy',
                             save_file=True, file_name=save_path+fname+'.png')

#ourLaser_50fs()
#ourLaser_35fs()
#oldRALLaser_40fs()
#RALBlueLightSource()
#newRALLaser()
#newRALLaser_smallerCapillary()
#Pharos()
Pharos_smallerCoreFibre()