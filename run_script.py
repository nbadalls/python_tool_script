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
    input_path = "/mnt/glusterfs/o2n/FaceRecognition/Train_Data/O2N_Patches/Patches_mtcnn/MultiPatches_list/single_folder_combine_add_list/AsianLife3W_GE15_list.txt"
    output_path = input_path.replace('.txt', '-batch3.txt')
    select_landmark = text_process.TextProcess(input_path, output_path)
    select_landmark.selected_certain_part_from_landmark_file('batch3', False)

def createlist():
      
      input_path = "/mnt/glusterfs/o2n/FaceRecognition/Train_Data/O2N_Patches/Patches_mtcnn/MultiPatches/fc_0.35_112x96/Data_sdc/IDLife-capture-30k"
      dst_path = "/mnt/glusterfs/o2n/FaceRecognition/Train_Data/O2N_Patches/Patches_mtcnn/MultiPatches_list/single_folder_combine_add_list"
            
      num = 15
      add_prefix = "Data_sdc"
      # create_list1 = ['2018-03-28_O2O_6000', 'ChinaMobile-pick2', 'Indonesia_Lib_Test', 'Migrant_Worker_select', 'Oriental', 'PadCollection2', 'PAKJ_09_09', 'XCH-select-2018']
      # create_list2 = ['Data_sdc/IDLife-capture-30k', 'Data_sdc/Life_beidi-pad-cap_130', ]

      get_list = create_list.CreateList(input_path, dst_path)
      get_list.create_condition_image_list(num, add_prefix)

      # add_prefix = None    
      # for elem in create_list2:

      # for  elem in os.listdir(input_path):
      #         # if elem.find('Data_sdc') < 0:
      #                 get_list = create_list.CreateList(input_path + '/' + elem, dst_path)
      #                 get_list.create_condition_image_list(num, add_prefix)

def create_label():

    image_list = "/mnt/glusterfs/o2n/FaceRecognition/Train_Data/O2N_Patches/Patches_mtcnn/MultiPatches_list/combine_folder_combine_add_list/combine_add_base-shot+Asia-b3+beid+cap+mul+Chinap2+Pad2+Padb3+XCH_GE15_list.txt"
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
    input_path = "/mnt/glusterfs/o2n/FaceRecognition/Train_Data/O2N/Drive_Data"
    output_path = "/home/hjg/Data/SDB_Disk/Data/Train_Data/O2N/Data_sdd/identification_driver_5W"
    select_image = select_image_files.SelectImages()
    #select_image.select_one_image_from_file(input_path,output_path, 50000 )
    select_image.select_certain_image_from_file(input_path, output_path, "2.jpg", 50000)

def combine_add_landmarks():
    input_path = "/mnt/glusterfs/o2n/FaceRecognition/TrainData_landmarks/single_mtcnn_landmark"
    add_landmark_path = "/mnt/glusterfs/o2n/FaceRecognition/TrainData_landmarks/single_mtcnn_landmark_add_detect"
    output_path = "/mnt/glusterfs/o2n/FaceRecognition/TrainData_landmarks/single_mtcnn_landmark_combine_detect"

    combine_landmark = text_process.TextProcess(input_path, output_path)
    combine_landmark.combine_landmarks_sort(add_landmark_path)
    
def select_face_recognition_result():
    input_path = "/home/zkx/Project/O2N/train_models/create_clean_list/Result/result_face_recognition_predict_2018-07-20_AMImageMtcnn-b0.35s30_fc_0.35_112x96_b+add1+Chinap2+XCH18-delAsia-b3_MobileFaceNet-bn_zkx_iter_170000.txt"
    possibilty = 0.0
    select_landmark = text_process.TextProcess(input_path)    
    select_landmark.select_face_recognition_result(possibilty)
    
    
def clean_list_certain_class_number_label():
    input_path = "/home/zkx/Project/O2N/train_models/create_clean_list/Result/result_face_recognition_predict_2018-07-20_AMImageMtcnn-b0.35s30_fc_0.35_112x96_b+add1+Chinap2+XCH18-delAsia-b3_MobileFaceNet-bn_zkx_iter_170000_correct_possi0.0_select.txt"
    create_clean_list = create_list.CreateList(input_path)
    create_clean_list.clean_list_certain_class_number_label(8)
    
    
    
if __name__ == '__main__':
    # images_select()
    #create_faceface_label()
   # create_image_pair()
     create_label()
    # run_script()
    # createlist()
    #combine_add_landmarks()
    # select_face_recognition_result()
    # clean_list_certain_class_number_label()
