#!/usr/bin/python

# Copyright (c) 2012, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All rights reserved.
#
# The NASA Tensegrity Robotics Toolkit (NTRT) v1 platform is licensed
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

""" Converts .nnw files to a JSON file """

# Purpose: Read JSON files and print results to the command line. Used to determine best params after learning has completed
# Author:  Brian Mirletz
# Date:    March 2015

import sys
import os
import subprocess
import json
import random
import logging
import collections
import operator


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    configFile = sys.argv[1]
    numFiles = int(sys.argv[2])
    
    scoreSum = 0
    fileSum = 0
    maxScore = 0
    
    paramList = []
    
    for i in range(0, numFiles):
        scoresPath = configFile + str(i) +'.json'
        fin = open(scoresPath, 'r')
        obj = json.load(fin)
        fin.close()
        try: 
            paramID = obj['feedbackVals']['paramID']
            if (paramList.count(paramID) == 0):
                thisScore = float(obj['feedbackVals']['avgScore'])
                fileSum += 1
                paramList.append(paramID)
            else:
                thisScore = 0
        except KeyError:
            thisScore =  0
        
        if(thisScore > maxScore):
            topScore = i
            maxScore = thisScore
            topObj = obj
        
        scoreSum += thisScore
        
    print(maxScore)
    print(scoreSum / fileSum)
    print(topScore)
    
    # Now average the scores of the top object
    
