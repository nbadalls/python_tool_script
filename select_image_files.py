# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:12:31 2018
use to select image from files
@author: minivision
"""


import shutil
import utility
import os
import sys

class SelectImages():
    def select_one_image_from_file(self, input_file, output_file, select_num):

        if not os.path.exists(input_file):
            print "{} is not exists".format(input_file)
            return

        utility.create_dir(output_file)
        counter = 1
        for root_path, folder_path, filenames in os.walk(input_file):

            if len(filenames) > 0:
		if counter > select_num:
			break

                if filenames[0].endswith('.jpg') or filenames[0].endswith('.png') or   \
                    filenames[0].endswith('.bmp') or  filenames[0].endswith('.JPG'):

                    image_path = '{}/{}'.format(root_path, filenames[0])
                    dst_image_name = str(counter).zfill(5)
                    dst_path = '{}/{}.jpg'.format(output_file, dst_image_name)
                    shutil.copy(image_path,dst_path)

                    sys.stdout.write('{}/{}\r'.format(counter, select_num))
                    sys.stdout.flush()
                    counter+=1


    def select_certain_image_from_file(self, input_file, output_file, select_image, select_num):

        if not os.path.exists(input_file):
            print "{} is not exists".format(input_file)
            return

        utility.create_dir(output_file)
        counter = 1
        for root_path, folder_path, filenames in os.walk(input_file):

          for elem in filenames:

               if elem == select_image:

                    image_path = '{}/{}'.format(root_path, elem)
                    dst_image_name = str(counter).zfill(5)
                    dst_path = '{}/{}d.jpg'.format(output_file, dst_image_name)
                    shutil.copy(image_path,dst_path)

                    sys.stdout.write('{}/{}\r'.format(counter, select_num))
                    sys.stdout.flush()
                    counter+=1

    def rename_image_names(self, input_file, output_file, image_prefix):
        if not os.path.exists(input_file):
                print "{} is not exists".format(input_file)
                return
        utility.create_dir(output_file)
        counter = 1
        for root_path, folder_path, filenames in os.walk(input_file):
            for elem in filenames:
                srcImage_path = '{}/{}'.format(root_path,elem)
                dst_name = str(counter).zfill(5)
                dst_path = '{}/{}-{}.jpg'.format(output_file, image_prefix, dst_name)
                shutil.copy(srcImage_path, dst_path)
                counter+=1
        print("Done!!")

    def extract_noface_image(self, image_list, root_path, dst_path):

        utility.create_dir(dst_path)
    	f = open(image_list, 'r')
    	data = f.read().splitlines()
    	f.close()

    	for index, elem in enumerate(data):
                     utility.show_process_percentage(index, len(data), 50)
                     srcimage_path = '{}/{}'.format(root_path, elem)
                     if os.path.isfile(srcimage_path):
                         dst_move_path = '{}/{}'.format(dst_path, elem.split('/')[-1])
                         shutil.move(srcimage_path, dst_move_path)
