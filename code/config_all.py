# -*- coding: utf-8 -*-

"""
For which systems the evaluation should be done.
It needs to be in the results dir defined in dataset_info.py
"""
RUN_FOR_SYSTEMS = ( "SochorCVIU_Edgelets_BBScale_Reg",
                    "SochorCVIU_ITS15_BVMC14",
                    "SochorCVIU_ManualCalib_ManualScale",
                    )

RUN_FOR_SYSTEMS = ["SochorCVIU_Edgelets_ManualScale",  "SochorCVIU_ITS15_ManualScale",
                   "SochorCVIU_ManualCalib_SpeedScale", "dubska_optimal_calib_vp2",
                   "SochorCVIU_Edgelets_SpeedScale", "SochorCVIU_ITS15_SpeedScale",
                   "dubska_bmvc14", "dubska_optimal_scale", "SochorCVIU_ITS15_BVMC14",
                   "SochorCVIU_ManualCalib_ManualScale",  "dubska_optimal_calib",
                   "dubska_optimal_scale_vp2", "VPout_VP1VP2_resnet_orig_normalized_aug_25.128in_1.0s_32b_2_r100_0.5c"]
                    
"""
For which video the evaluation should be done. 
You can use keys A,B or C.
See dataset_info.py for more information and 
training videos for each splitting
"""
RUN_FOR_VIDEOS = SPLIT_TEST_VIDEOS["C"]


"""
Defines systems and thresholds
If a speed estmiation error for a system in the set is larger
then the threshold, the trajectory is shown
WARNING: You need to delete the cached results (or use -rc argument)
"""
SHOW_BAD_FOR_SYSTEMS = set()
SHOW_BAD_THRESHOLD = 30


"""
If true, vehicles' trajectories for which the computation
of intersections wihh measurement lines failes are shown
WARNING: You need to delete the cached results (or use -rc argument)
"""
SHOW_ERRORS = False



#%%
"""
##############################################################
################### PRESENTATION HELPER FUNCTIONS ############
##############################################################
"""

"""
Conversions for plotting and printing statistics
"""
def labelConversion(systemId):
    return systemId

"""
Styles for cumulative histograms
"""
def plotStyleCumulativeHist(systemId):
    styleDict = {"linewidth":2}
    return styleDict


"""
Styles for error histograms
"""
def plotStyleErrorHist(systemId):
    styleDict = {"linewidth":2}
    return styleDict
    
