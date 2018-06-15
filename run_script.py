# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:41:45 2018

@author: zkx-97
"""

import text_process
import create_list

def run_script():
    input_path = "/home/zkx/Data_sdb/TrainData_landmarks/single_mtcnn_landmark/Life_beidi-pad-cap_130_landmarks.txt"
    output_path = input_path.replace('.txt', '_select.txt')
    select_landmark = text_process.TextProcess(input_path, output_path)
    select_landmark.selected_certain_part_from_landmark_file('.JPG')
    
def createlist():
    
      input_path = "/home/zkx/Data_sdb/TrainData/shot1600"
      dst_path = "/home/zkx/Data_sdb/TrainData/Data_sdd/Patches_mtcnn/MultiPatches_list/single_folder_list"
      get_list = create_list.CreateList(input_path, dst_path)
      
      num = 10
      add_prefix = None
      get_list.create_condition_image_list(num, add_prefix)
      
if __name__ == '__main__':
    
    createlist()