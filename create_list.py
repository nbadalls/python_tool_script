# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:44:12 2018

@author: zkx-97
"""


import os 
import utility

class CreateList:
    
    def __init__(self, input_folder_path, dst_folder_path):
        
        utility.create_dir(dst_folder_path)
        input_folder_path = input_folder_path.rstrip('/')
        
        self.input_folder_path = input_folder_path
        self.dst_folder_path = dst_folder_path
        
                    
# according to condition to make image list, based on image's number in each folder
    def create_condition_image_list(self, num, add_prefix = None):
        
       print "input folder: {}".format(self.input_folder_path)
       folder_name = self.input_folder_path.split('/')[-1]
      
       dst_file_path = '{}/{}_GE{}_list.txt'.format(self.dst_folder_path, folder_name, num)
       
       print "save into path: {}".format(dst_file_path)
       f = open(dst_file_path, 'w')
       
       print "save list result.."
       for root_path, folder_path, filenames in os.walk(self.input_folder_path):
          #condition
          if len(filenames) >= int(num):
             for elem in filenames:
                 if elem.endswith('.txt'):
                     continue
                 #get path prefix
                 path_prefix = root_path.split(self.input_folder_path + '/')[-1]
                 save_path = '{}/{}'.format(path_prefix, elem)
                 if add_prefix != None:
                     save_path = add_prefix + '/' + save_path
                 f.write('{}\n'.format(save_path))  
                 
       print "Done!"
       f.close()
                   
            
        
        