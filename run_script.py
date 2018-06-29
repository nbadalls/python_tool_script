# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:41:45 2018

@author: zkx-97
"""

import text_process
import create_list
import select_image_files
import os

def run_script():
    input_path = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/Patches_mtcnn/MultiPatches_list/single_folder_list/AsianLife3W_GE8_list.txt"
    output_path = input_path.replace('.txt', '_batch1-2.txt')
    select_landmark = text_process.TextProcess(input_path, output_path)
    select_landmark.selected_certain_part_from_landmark_file('batch3', False)

def createlist():
      
     
      input_path = "/home/minivision/Data/FakeFace/Train_mtcnn_patches/fc_0.35_112x96"
      dst_path = "/home/minivision/Data/FakeFace/Train_mtcnn_patches/single_folder_list"
      
          
      num = 0
      add_prefix = None
      
      for elem in os.listdir(input_path):

         # if elem.find('Data_sdc') < 0:
              get_list = create_list.CreateList(input_path + '/' + elem, dst_path)
              get_list.create_condition_image_list(num, add_prefix)

def create_label():

    image_list = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/Patches_mtcnn/MultiPatches_list/combine_folder_list/combine_mtcnn_base+add1-2_GE8_list.txt"
    get_label = create_list.CreateList()
    get_label.create_patch_label_from_list(image_list)


def create_image_pair():
    image_list = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH_PAD_01_23/XCH-big-mtcnn_list.txt"
    get_image_pair_list = create_list.CreateList()
    get_image_pair_list.create_pair_list(image_list)
    
def create_faceface_label():
    landmark_path = "/media/minivision/OliverSSD/LiveBody/Testset/Test7_smalllandmark_result/Test7_small_landmarks.txt"
    get_fakeface_label = create_list.CreateList()
    get_fakeface_label.create_fakeface_label_from_landmark(landmark_path)
    
def clean_landmark():
    landmark_path = "/home/minivision/Data/FakeFace/Train_mtcnn_combine_landmark/2018-06-22_combine_FakeFace_landmarks.txt"
    get_fakeface_label = create_list.CreateList()
    get_fakeface_label.clean_unregular_landmark_items(landmark_path, False)
    
def images_select():
    input_path = "/mnt/glusterfs/o2n1/FaceRecognition/Train_Data/O2N/IDID1v1-clear-10k"
    output_path = "/media/minivision/OliverSSD/Data/identification_id_clear_5W"
    select_image = select_image_files.SelectImages()
    select_image.select_one_image_from_file(input_path,output_path, 500 )

if __name__ == '__main__':
    images_select()
    #create_faceface_label()
   # create_image_pair()
    #create_label()
    #run_script()
    #createlist()
