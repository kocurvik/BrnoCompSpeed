# -*- coding: utf-8 -*-
import os
import platform
    

"""
Paths to dataset and result dir
"""
if platform.system() == "Windows":        
    TRANS_PATH = lambda p: p
else:
    TRANS_PATH = lambda p: p

DATASET_BASE_PATH = TRANS_PATH("D:/Skola/PhD/data/2016-ITS-BrnoCompSpeed/dataset/")
RESULTS_DIR = TRANS_PATH("D:/Skola/PhD/data/2016-ITS-BrnoCompSpeed/results/")

# DATASET_BASE_PATH = TRANS_PATH("/home/k/kocur15/data/2016-ITS-BrnoCompSpeed/dataset/")
# RESULTS_DIR = TRANS_PATH("/home/k/kocur15/data/2016-ITS-BrnoCompSpeed/results/")


DATASET_SESSIONS = {
    "session0": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 25.0},
            "right": {"fps": 50.0}
        }
        
    },
    "session1": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 50.0},
            "right": {"fps": 50.0}
        }
    },
    "session2": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 50.0},
            "right": {"fps": 50.0}
        }
    },
    "session3": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 50.0},
            "right": {"fps": 50.0}
        }
    },
    "session4": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 50.0},
            "right": {"fps": 50.0}
        }
    },
    "session5": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 50.0},
            "right": {"fps": 50.0}
        }
    },
    "session6": {
        "recordings": {        
            "left": {"fps": 50.0},
            "center": {"fps": 50.0},
            "right": {"fps": 50.0}
        },
        "invalidLanes": set([2])
        
    }
    
}





ALL_SESSIONS = set(DATASET_SESSIONS.keys())

ALL_VIDEOS = []
#ALL_VIDEOS.append(("session5","left"))
for _sId in sorted(DATASET_SESSIONS):
#    if _sId == "session5":
#        for _rId in ("center", "right"):
#            ALL_VIDEOS.append((_sId, _rId))
#    else:
#        for _rId in ("left", "center", "right"):
#            ALL_VIDEOS.append((_sId, _rId))
    for _rId in ("left", "center", "right"):
        ALL_VIDEOS.append((_sId, _rId))
       

SPLIT_TRAIN_SESSIONS = {}
SPLIT_TRAIN_SESSIONS["A"] = {"session0"}
SPLIT_TRAIN_SESSIONS["B"] = SPLIT_TRAIN_SESSIONS["A"] | {"session1", "session2"}
SPLIT_TRAIN_SESSIONS["C"] = SPLIT_TRAIN_SESSIONS["B"] | {"session3"}
SPLIT_TRAIN_SESSIONS["K"] = SPLIT_TRAIN_SESSIONS["C"] | {"session4", "session5"}
SPLIT_TRAIN_SESSIONS["L"] = SPLIT_TRAIN_SESSIONS["C"] | {"session5", "session6"}


SPLIT_TEST_SESSIONS = dict(map(lambda i: (i[0], ALL_SESSIONS-i[1]), SPLIT_TRAIN_SESSIONS.iteritems()))

SPLIT_TRAIN_VIDEOS = dict(map(lambda i: (i[0], filter(lambda j: j[0] in i[1], ALL_VIDEOS)), SPLIT_TRAIN_SESSIONS.iteritems()))
SPLIT_TEST_VIDEOS = dict(map(lambda i: (i[0], filter(lambda j: j[0] in i[1], ALL_VIDEOS)), SPLIT_TEST_SESSIONS.iteritems()))

def getPathForRecording(session, recording):
    return os.path.join(DATASET_BASE_PATH, "%s_%s"%(session, recording))
