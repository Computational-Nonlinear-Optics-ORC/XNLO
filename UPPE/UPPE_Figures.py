# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:05:53 2018

@author: sam
"""

from UPPEPostprocessing import UPPE
import numpy as np

import gc

def single(start=1, end=101):
  from UPPEPostprocessing import UPPE

  prop_step=1
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  step_size = 1

  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  import numpy as np
  
  x_range = (0.0035, 0.070)

  for i in range(start, end, step_size):
    prop_step = i

    files = {"A_w_R":"../../Results/UPPE/800nm_ourLaser/50fs/0.8W/data/000_"+str(prop_step)+"_A_w_R.bin",
             "A_w_I":"../../Results/UPPE/800nm_ourLaser/50fs/0.8W/data/000_"+str(prop_step)+"_A_w_I.bin",
             "w_active":"../../Results/UPPE/800nm_ourLaser/50fs/0.8W/data/000_"+str(prop_step)+"_w_active.bin",
             "ionisation":"../../Results/UPPE/800nm_ourLaser/50fs/0.8W/data/000_"+str(prop_step)+"_electron_density.bin"}

    parameters = {"radius":75.0e-6,
                  "N_t":50000,
                  "Z":0.07,
                  "Z_min":0.0035,
                  "N_z":100,
                  "w_active_min_index":32}
    run_000 = UPPE(files=files, parameters=parameters, labels="800", format=False)

    save_path = '../../Results/UPPE/800nm_ourLaser/50fs/0.8W/animations/source/'
    fname = 'intensity_wavelength_mode_'
    run_000.plot.intensity_wavelength(xlim=(400, 1000,),#xlim=(10, 150), ylim=(0, 0.5e-15),
                                    representation="mode", save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')
    fname = 'intensity_wavelength_radial_'
    run_000.plot.intensity_wavelength(xlim=(400, 1000),#xlim=(10, 150), ylim=(0, 0.5e-15),
                                    representation="radial", save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')
    fname = 'intensity_wavelength_mradial_radialluWeighted_'
    run_000.plot.intensity_wavelength(xlim=(400, 1000),#xlim=(10, 150), ylim=(0, 0.5e-15),
                                    representation="radial",
                                    radially_weighted=True, save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')
    fname = 'intensity_time_mode_'
    run_000.plot.intensity_time(xlim=(-100.0e-15, 100.0e-15),
                              representation="mode",
                              field="envelope", save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')
    fname = 'intensity_radial_'
    run_000.plot.intensity_time(xlim=(-100.0e-15, 100.0e-15),
                              representation="radial",
                              field="envelope", save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')
    fname = 'time_radialDistance_'
    run_000.plot.time_radialDistance(x_step_size=10, save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')#, xlim=(-100e-15, 100e-15))

def multi_wavelength():

  prop_step = 1
  
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  prop_step = 100
  step_size = 1
  
  from UPPEPostprocessing import UPPE
  import numpy as np
  
  x_range = (0.0035, 0.070)
  
  path = '../../Results/UPPE/800nm_ourLaser/50fs/varyingPower/data/'#"./output/"
  #path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz200_20modes/data/"+sim_run+"/"
  #path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
  
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  step_size = 1
  
  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}
  
  save_path = '../../Results/UPPE/800nm_ourLaser/50fs/varyingPower/'
  fname = 'intensityWavelength_comparison'

  files_A_w_R = np.array(path+"003"+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+"003"+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+"003"+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+"003"+"_"+str(prop_step)+"_electron_density.bin")
  
  labels = np.array(str(0.4)+"W")
  
  for i in range(2, 4+1, step_size):

    sim_run = str("{0:0=3d}".format(i*4))
    
    files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
    files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
    files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
    files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

    labels = np.vstack((labels, np.array(str((i*4)/10.0)+"W")))

  labels=labels[:, 0]

  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}
  
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)

  multiple_runs.plot.combined_intensity_wavelength(xlim=(400, 1000),
                                                   representation="mode",
                                                   show_labels=True,
                                                   save_file=True, file_name=save_path+fname+'.png')
                                                             
  run_000 = None    
  del run_000
  gc.collect()

def multi_wavelength_pressure():

  prop_step = 1
  
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  prop_step = 100
  step_size = 1
  
  from UPPEPostprocessing import UPPE
  import numpy as np
  
  x_range = (0.0035, 0.070)
  
  path = '../../Results/UPPE/800nm_ourLaser/50fs/varyingPressure/data/'#"./output/"
  #path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz200_20modes/data/"+sim_run+"/"
  #path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
  
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  step_size = 1
  
  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}
  
  save_path = '../../Results/UPPE/800nm_ourLaser/50fs/varyingPressure/'
  fname = 'intensityWavelength_pressure_comparison'

  files_A_w_R = np.array(path+"004"+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+"004"+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+"004"+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+"004"+"_"+str(prop_step)+"_electron_density.bin")
  
  labels = np.array(str(25)+"mBar")
  
  for i in range(2, 4+1, step_size):

    sim_run = str("{0:0=3d}".format(i*5 - 1))
    
    files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
    files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
    files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
    files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

    labels = np.vstack((labels, np.array(str((i*5 - 1)*5+5)+"mBar")))

  labels=labels[:, 0]

  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}
  
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)

  multiple_runs.plot.combined_intensity_wavelength(xlim=(400, 1000),
                                                   representation="mode",
                                                   show_labels=True,
                                                   save_file=True, file_name=save_path+fname+'.png')
                                                             
  run_000 = None    
  del run_000
  gc.collect()

def multi_wavelength_FWHM():

  prop_step = 1
  
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  prop_step = 100
  step_size = 1
  
  from UPPEPostprocessing import UPPE
  import numpy as np
  
  x_range = (0.0035, 0.070)
  
  path = '../../Results/UPPE/800nm_ourLaser/varyingFWHM/data/'#"./output/"
  #path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz200_20modes/data/"+sim_run+"/"
  #path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
  
  start_position = 0.0
  finish_position = 0.0750
  n_z = 100
  
  step_size = 1
  
  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}
  
  save_path = '../../Results/UPPE/800nm_ourLaser/varyingFWHM/'
  fname = 'intensityWavelength_FWHM_comparison'

  files_A_w_R = np.array(path+"003"+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+"003"+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+"003"+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+"003"+"_"+str(prop_step)+"_electron_density.bin")
  
  labels = np.array(str(20)+"fs")
  
  for i in range(2, 4+1, step_size):

    sim_run = str("{0:0=3d}".format(i*3))
    
    files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
    files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
    files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
    files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

    labels = np.vstack((labels, np.array(str((i*3)*5+5)+"fs")))

  labels=labels[:, 0]

  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}
  
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)

  multiple_runs.plot.combined_intensity_wavelength(xlim=(400, 1000),
                                                   representation="mode",
                                                   show_labels=True,
                                                   save_file=True, file_name=save_path+fname+'.png')
                                                             
  run_000 = None    
  del run_000
  gc.collect()


def multi_intensity_radialDistance_power():

  prop_step = 100

  dir = '../../Results/UPPE/800nm_ourLaser/50fs/varyingPower/data/'
  fwhm = "50fs/"
  files_A_w_R = np.array(dir+"0"+str(0)+str(0)+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(dir+"0"+str(0)+str(0)+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(dir+"0"+str(0)+str(0)+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(dir+"0"+str(0)+str(0)+"_"+str(prop_step)+"_electron_density.bin")
  max_file_name = 24

  n_z = 100

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
          if j*10 + i <= max_file_name and j+i > 0:
              files_A_w_R = np.vstack((files_A_w_R, (dir+"0"+str(j)+str(i)+"_"+str(prop_step)+"_A_w_R.bin")))
              files_A_w_I = np.vstack((files_A_w_I, (dir+"0"+str(j)+str(i)+"_"+str(prop_step)+"_A_w_I.bin")))
              files_w_active = np.vstack((files_w_active, (dir+"0"+str(j)+str(i)+"_"+str(prop_step)+"_w_active.bin")))
              files_electronDensity = np.vstack((files_electronDensity, (dir+"0"+str(j)+str(i)+"_"+str(prop_step)+"_electron_density.bin")))
              
              lamda = lamda + (wavelength, )
              RR = RR + (rep_rate, )
              FWHM = FWHM + (pulse_length, )
              spot_radius = spot_radius + (radius, )
          if j*10 + i > max_file_name:
              break

  #simulation_parameters = {'lamda':lamda,
  #                         'P_av':(0.4, 0.8, 1.2, 1.6, 2.0,
  #                                 2.4, 2.8, 3.2, 3.6, 4.0,
  #                                 4.4, 4.8, 5.2, 5.6, 6.0,
  #                                 6.4, 6.8, 7.2, 7.6, 8.0),
  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  labels=()

  save_path = '../../Results/UPPE/800nm_ourLaser/50fs/varyingPower/'
  fname = 'combined_intensity_radialDistance_power'

  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_intensity_radialDistance_power(save_file=True, file_name=save_path+fname+'.png')

def ionisation_40fs_800nm_0_4W():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.070)

  sim_run = "001"
  path = "./output/"
  path = "../../Results/UPPE/40fsFWHM/Power_Pressure_comparisons/P0.4W/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.075
  n_z = 100

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/40fsFWHM/Power_Pressure_comparisons/P0.4W/'
  fname = 'electronDensity_radialDistance_propagationDistance'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_electronDensity_colourMap(radially_weighted=True, save_file=True, file_name=save_path+fname+'.png')

def ionisation_40fs_800nm_0_8W():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.070)

  sim_run = "003"
  path = "./output/"
  path = "../../Results/UPPE/40fsFWHM/Power_Pressure_comparisons/P0.8W/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.075
  n_z = 100

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/40fsFWHM/Power_Pressure_comparisons/P0.8W/'
  fname = 'electronDensity_radialDistance_propagationDistance'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_electronDensity_colourMap(radially_weighted=True, save_file=True, file_name=save_path+fname+'.png')

def ionisation_5fs_800nm_0_4W():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.070)

  sim_run = "001"
  path = "./output/"
  path = "../../Results/UPPE/5fsFWHM/Power_Pressure_comparisons/P0.4W/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.075
  n_z = 100

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/5fsFWHM/Power_Pressure_comparisons/P0.4W/'
  fname = 'electronDensity_radialDistance_propagationDistance'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_electronDensity_colourMap(radially_weighted=True, save_file=True, file_name=save_path+fname+'.png')

def mode_interaction_20m():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.070)

  sim_run = "000"
  path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.075
  n_z = 1000

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/'
  fname = 'propagationDistance_intensity_on-ishAxis_zSteps1000'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_Intensity(x_range=x_range,
                                                            #xlim=(0.0035, 0.07),
                                                            #ylim=(0.0E22, 3.0E22),
                                                            representation="radial",
                                                            position="on-axis",
                                                            save_file=True, file_name=save_path+fname+'.png')

def mode_interaction_2m():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.070)

  sim_run = "000"
  path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.075
  n_z = 1000

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/'
  fname = 'propagationDistance_intensity_on-ishAxis_zSteps1000'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_Intensity(x_range=x_range,
                                                            #xlim=(0.0035, 0.07),
                                                            #ylim=(0.0E22, 3.0E22),
                                                            representation="radial",
                                                            position="on-axis",
                                                            save_file=True, file_name=save_path+fname+'.png')

def mode_interaction_40fs_pcolor():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.07)

  sim_run = "002"
  path = "../../Results/UPPE/40fsFWHM/zeroPressure_lowPower_nz100_40modes/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.07
  n_z = 100

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/40fsFWHM/zeroPressure_lowPower_nz100_40modes/'
  fname = 'propagationDistance_radialDistance_intensity_radiallyWeighted'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_radialDistance(x_range=x_range, radially_weighted=True,
                                                                 save_file=True, file_name=save_path+fname+'.png')

def mode_interaction_5fs_pcolor():
  from UPPEPostprocessing import UPPE
  import numpy as np

  x_range = (0.0035, 0.07)

  sim_run = "000"
  path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz100_40modes/data/"+sim_run+"/"
  prop_step = 1

  start_position = 0.0
  finish_position = 0.07
  n_z = 100

  prop_step = 1
  step_size = 1
  files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")
  files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")
  files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_w_active.bin")
  files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_electron_density.bin")

  labels = np.array(str((finish_position - start_position) / n_z * prop_step))

  for i in range(2, n_z+1, step_size):
      prop_step = i
      
      files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_A_w_R.bin")))
      files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_A_w_I.bin")))
      files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_w_active.bin")))
      files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_electron_density.bin")))

      labels = np.vstack((labels, np.array(str((finish_position - start_position) / n_z * prop_step))))
      
  files = {"A_w_R":files_A_w_R,
           "A_w_I":files_A_w_I,
           "w_active":files_w_active,
           "ionisation":files_electronDensity}

  parameters = {"N_t":16384,  # To match the UPPE config file
                "radius":75.0e-6,
                "Z":0.07,
                "Z_min":0.0035,
                "N_z":n_z,
                "w_active_min_index":32}

  save_path = '../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz100_40modes/'
  fname = 'propagationDistance_radialDistance_intensity_radiallyWeighted'
  multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
  multiple_runs.plot.combined_propagationDistance_radialDistance(x_range=x_range, radially_weighted=True,
                                                                 save_file=True, file_name=save_path+fname+'.png')
#multi_intensity_radialDistance_power()
#multi_wavelength()
#multi_wavelength_pressure()
#multi_wavelength_FWHM()
#multi_wavelength()
#ionisation_40fs_800nm_0_4W()
#ionisation_40fs_800nm_0_8W()
#ionisation_5fs_800nm_0_4W()
#mode_interaction_20m()
#mode_interaction_2m()
#mode_interaction_40fs_pcolor()
mode_interaction_5fs_pcolor()