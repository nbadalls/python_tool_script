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
            print (root_path)
            if len(filenames) > 0 and counter <=select_num:
                if filenames[0].endswith('.jpg') or filenames[0].endswith('.png') or   \
                    filenames[0].endswith('.bmp') or  filenames[0].endswith('.JPG'):
        
                    image_path = '{}/{}'.format(root_path, filenames[0])
                    dst_image_name = str(counter).zfill(5)
                    dst_path = '{}/{}.jpg'.format(output_file, dst_image_name)
                    shutil.copy(image_path,dst_path)
                    
                    sys.stdout.write('{}/{}\r'.format(counter, select_num))
                    sys.stdout.flush()
                    counter+=1
                
    
                
                
                
                
        
