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


      input_path = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH_PAD_07-24_outdoor/mtcnn_patches/fc_0.35_112x96/image_life_range"
      dst_path = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH_PAD_07-24_outdoor/mtcnn_patches/fc_0.35_112x96"


      num = 0
      add_prefix = None
      get_list = create_list.CreateList(input_path, dst_path)
      get_list.create_condition_image_list(num, add_prefix)

    #   for elem in os.listdir(input_path):

         # if elem.find('Data_sdc') < 0:
            #   get_list = create_list.CreateList(input_path + '/' + elem, dst_path)
            #   get_list.create_condition_image_list(num, add_prefix)

def create_label():

    image_list = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH_PAD_08-01_outdoor/XCH_PAD_07-24_outdoor_list.txt"
    get_label = create_list.CreateList()
    get_label.create_patch_label_from_list(image_list)


def create_image_pair():
    image_list = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH_PAD_08-01_outdoor/XCH_PAD_07-24_outdoor_list.txt"
    get_image_pair_list = create_list.CreateList()
    get_image_pair_list.create_pair_list(image_list)

def create_faceface_label():
    landmark_path = "/media/minivision/OliverSSD/LiveBody/Testset/Test7_xch/patches-mtcnn/image_list/2018-07-02_test7_xch-pad_imagelist.txt"
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

def rename_images():
    input_path = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH-small-outdoor/select_small_testset_img"
    output_path = "/media/minivision/OliverSSD/FaceRecognition/TestSet/XCH-small-outdoor/select_small_testset_img_rename"
    image_prefix = "2018-07-02_pad"
    select_image = select_image_files.SelectImages()
    select_image.rename_image_names(input_path, output_path, image_prefix)

def select_Noface_image():
    image_list = "/media/minivision/SSD-Kaixiang/2018-07-25_add_testSet/combine_name_mtcnn_result/combine_name_missface.txt"
    root_path = "/media/minivision/SSD-Kaixiang/2018-07-25_add_testSet"
    dst_path = "/media/minivision/SSD-Kaixiang/2018-07-25_add_testSet/missface"
    select_image = select_image_files.SelectImages()
    select_image.extract_noface_image(image_list, root_path, dst_path)
if __name__ == '__main__':
   # images_select()
   #create_faceface_label()
    create_image_pair()
    # create_label()
    #run_script()
    # createlist()
   #rename_images()
     #select_Noface_image()
