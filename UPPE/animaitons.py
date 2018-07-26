# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:05:53 2018

@author: sam
"""

from UPPEPostprocessing import UPPE
import numpy as np

import gc

def HHG_time_radialDistance(start=1, end=100):
    x_range = (0.0035, 0.070)
    
    sim_run = "002"
    path = '../../Results/UPPE-XNLO/400nm_RALBlueLight/30fs/0.8W/data/'
    #path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz200_20modes/data/"+sim_run+"/"
    #path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
    prop_step = 1
    
    start_position = 0.0
    finish_position = 0.0750
    n_z = 100
    
    prop_step = 1
    step_size = 1
    #files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_R.bin")
    #files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_I.bin")
    #files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_w.bin")
    #files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_E.bin")
    #
    #labels = np.array(str((finish_position - start_position) / n_z * prop_step))
    
    save_path = '../../Results/UPPE-XNLO/400nm_RALBlueLight/30fs/0.8W/animations/source/'
    fname = 'HHG_time_radialDistance_'
    
    for i in range(start, end, step_size):
        prop_step = i
        
        files = {"A_w_R":path+str(sim_run)+"_"+str(prop_step)+"_HHG_R.bin",
                 "A_w_I":path+str(sim_run)+"_"+str(prop_step)+"_HHG_I.bin",
                 "w_active":path+str(sim_run)+"_"+str(prop_step)+"_HHG_w.bin",
                 "ionisation":path+str(sim_run)+"_"+str(prop_step)+"_HHG_E.bin"}
        
        parameters = {"radius":75.0e-6,
                      "N_t":50000,
                      "Z":0.07,
                      "Z_min":0.0035,
                      "N_z":100,
                      "w_active_min_index":32}
        
        files_A_w_R = path+sim_run+"_"+str(prop_step)+"_HHG_R.bin"
        files_A_w_I = path+sim_run+"_"+str(prop_step)+"_HHG_I.bin"
        files_w_active = path+sim_run+"_"+str(prop_step)+"_HHG_w.bin"
        files_electronDensity = path+sim_run+"_"+str(prop_step)+"_HHG_E.bin"
    
        labels = str((finish_position - start_position) / n_z * prop_step)
        
        
        run_000 = UPPE(files=files, parameters=parameters, labels="400", format=False)
        run_000.plot.time_radialDistance(x_step_size=10, z_max=0.9E-20, save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')#, xlim=(-100e-15, 100e-15))
        run_000 = None    
        del run_000
        
        gc.collect()
    
def HHG_propagationDistance_radialDistance():
    x_range = (0.0035, 0.070)
    
    sim_run = "001"
    path = "./output/"
    #path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz200_20modes/data/"+sim_run+"/"
    #path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
    prop_step = 1
    
    start_position = 0.0
    finish_position = 0.0750
    n_z = 100
    
    prop_step = 1
    step_size = 1
    
    from UPPEPostprocessing import UPPE
    import numpy as np
    
    x_range = (0.0035, 0.070)
    
    sim_run = "002"
    path = '../../Results/UPPE-XNLO/400nm_RALBlueLight/30fs/0.8W/data/'#"./output/"
    #path = "../../Results/UPPE/5fsFWHM/zeroPressure_lowPower_nz200_20modes/data/"+sim_run+"/"
    #path = "../../Results/UPPE/5fsFWHM/zeroPressure_nz1000/data/"+sim_run+"/"
    prop_step = 1
    
    start_position = 0.0
    finish_position = 0.0750
    n_z = 100
    
    prop_step = 1
    step_size = 1
    files_A_w_R = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_R.bin")
    files_A_w_I = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_I.bin")
    files_w_active = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_w.bin")
    files_electronDensity = np.array(path+sim_run+"_"+str(prop_step)+"_HHG_E.bin")
    
    labels = np.array(str((finish_position - start_position) / n_z * prop_step))
    
    for i in range(2, n_z+1, step_size):
        prop_step = i
        
        files_A_w_R = np.vstack((files_A_w_R, (path+sim_run+"_"+str(prop_step)+"_HHG_R.bin")))
        files_A_w_I = np.vstack((files_A_w_I, (path+sim_run+"_"+str(prop_step)+"_HHG_I.bin")))
        files_w_active = np.vstack((files_w_active, (path+sim_run+"_"+str(prop_step)+"_HHG_w.bin")))
        files_electronDensity = np.vstack((files_electronDensity, (path+sim_run+"_"+str(prop_step)+"_HHG_E.bin")))
    
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
    
    save_path = '../../Results/UPPE-XNLO/400nm_RALBlueLight/30fs/0.8W/animations/source/'
    fname = 'HHG_propagationDistance_radialDistance_'
    
    multiple_runs = UPPE(files=files, parameters=parameters, labels=labels)
    
    for i in range(1, 23, step_size):
        prop_step = i
        multiple_runs.plot.combined_propagationDistance_radialDistance(representation='spectral',
                                                                       field='carrier',
                                                                       x_range=x_range,
                                                                       #z_max=1e-3,
                                                                       window=(prop_step*5e-9, (prop_step+1)*5e-9),
                                                                       radially_weighted=True,
                                                                       save_file=True, file_name=save_path+fname+str("{0:0=3d}".format(prop_step))+'.png')
                                                               
    run_000 = None    
    del run_000
    gc.collect()

#HHG_time_radialDistance(start=1, end=15)
#HHG_time_radialDistance(start=15, end=30)
#HHG_time_radialDistance(start=30, end=45)
#HHG_time_radialDistance(start=66, end=70)
#HHG_time_radialDistance(start=70, end=83)
#HHG_time_radialDistance(start=83, end=98)
#HHG_time_radialDistance(start=98, end=101)
HHG_propagationDistance_radialDistance()