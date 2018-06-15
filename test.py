# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:51:11 2018

@author: zkx-97
"""

import os
path = "/home/zkx/Data_sdb/TrainData/shot1600"

for root , folder ,filename in os.walk(path):
    if len(filename) >0:
        print root