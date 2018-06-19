# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:41:45 2018

@author: zkx-97
"""

import text_process
import create_list
import os

def run_script():
    input_path = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/Patches_mtcnn/MultiPatches_list/single_folder_list/AsianLife3W_GE8_list.txt"
    output_path = input_path.replace('.txt', '_batch1-2.txt')
    select_landmark = text_process.TextProcess(input_path, output_path)
    select_landmark.selected_certain_part_from_landmark_file('batch3', False)
    
def createlist():
      
     
      input_path = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/Patches_mtcnn/MultiPatches/fc_0.35_112x96/Data_sdc"
      dst_path = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/Patches_mtcnn/MultiPatches_list/single_folder_list"
      
          
      num = 8
      add_prefix = "Data_sdc"
      
      for elem in os.listdir(input_path):
         
         # if elem.find('Data_sdc') < 0:
              get_list = create_list.CreateList(input_path + '/' + elem, dst_path)
              get_list.create_condition_image_list(num, add_prefix)
              
def create_label():
    
    image_list = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/Patches_mtcnn/MultiPatches_list/combine_folder_list/combine_mtcnn_base+add1-2_GE8_list.txt"
    get_label = create_list.CreateList()
    get_label.create_patch_label_from_list(image_list)
    

def create_image_pair():
    image_list = "/home/hjg/Data/SDB_Disk/Data/Test_Data/O2N/XCH-small/image_list-mtcnn.txt"
    get_image_pair_list = create_list.CreateList()
    get_image_pair_list.create_pair_list(image_list)
      
if __name__ == '__main__':
    
    create_image_pair()
    #create_label()
    #run_script()
    #createlist()