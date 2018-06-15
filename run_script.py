# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:41:45 2018

@author: zkx-97
"""

import text_process

def run_script():
    input_path = "/home/zkx/Data_sdb/TrainData_landmarks/single_mtcnn_landmark/Life_beidi-pad-cap_130_landmarks.txt"
    output_path = input_path.replace('.txt', '_select.txt')
    select_landmark = text_process.TextProcess(input_path, output_path)
    select_landmark.selected_certain_part_from_landmark_file('.JPG')
    
    
    
if __name__ == '__main__':
    
    run_script()