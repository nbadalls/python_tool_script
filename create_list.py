# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:44:12 2018

@author: zkx-97
"""


import os 
import utility
import sys


class CreateList:
    
    def __init__(self, input_folder_path = "", dst_folder_path = ""):
        
        if dst_folder_path != "":
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
                 if root_path != self.input_folder_path:
                     path_prefix = root_path.split(self.input_folder_path + '/')[-1]
                     save_path = '{}/{}/{}'.format(folder_name, path_prefix, elem)
                 else:
                     save_path = '{}/{}'.format(folder_name, elem)
                     
                 if add_prefix != None:
                     save_path = add_prefix + '/' + save_path
                 f.write('{}\n'.format(save_path))  
                 
       print "Done!"
       f.close()
 

      
    #create label from list
    def create_patch_label_from_list(self, crop_list):
         
         data = utility.read_file(crop_list)
         
         dst_path = crop_list.replace('.txt', '_label.txt')
         f = open(dst_path, 'w')
    
         common_prefix = os.path.abspath(os.path.join(data[0], ".."))
         counter = 0
         for index, elem in enumerate(data):
                elem_prefix = os.path.abspath(os.path.join(elem, ".."))
                if elem_prefix !=  common_prefix:
                    common_prefix = elem_prefix
                    counter +=1
             
                f.write('{} {}\n'.format(elem, counter))  
                sys.stdout.write('{}/{}\r'.format(index, len(data)-1))
                sys.stdout.flush()
    
         f.close() 
         
    def create_pair_list(self, image_list_path, imageid_prefix = 'id', imagelife_prefix='life'):
        
        data = utility.read_file(image_list_path)
        list_id = []
        list_life = []
        for line in data:
            if line.find(imageid_prefix) >=0 :
                list_id.append(line)
            elif line.find(imagelife_prefix) >=0:
                list_life.append(line)
            else:
                print 'no {} or {} exist in {}'.format(imageid_prefix, imagelife_prefix, line)
        
        dst_image_pair_list = image_list_path.replace('.txt', 'pair.txt')
        f = open(dst_image_pair_list, 'w')
        for index, life_elem in enumerate(list_life):
            for id_elem in list_id:
                id_name = id_elem.split('/')[-1].split('_')[0]
                life_name = life_elem.split('/')[-1].split('_')[0]
                if id_name == life_name:
                    label = 1
                else:
                    label = 0
                    
                f.write('{} {} {}\n'.format(life_elem, id_elem, label))
            utility.show_process_percentage(index, len(list_life)-1, 500)
        f.close()


    #create label from landmark (use to create fake face landmark)
    def create_fakeface_label_from_landmark(self, landmark_path):
        label_path = landmark_path.replace('.txt', '_label.txt')
        f = open(label_path, 'w')
        data = utility.read_file(landmark_path)
        for index, elem in enumerate(data):
            image_path = elem.split(' ')[0]
            label = image_path.split('/')[0].split('_')[0]
            f.write('{} {}\n'.format(image_path, label))
            utility.show_process_percentage(index, len(data)-1, 500)
            
        f.close()
 

#clean the elem which not equal to 11     
# "1/652125199710100815.jpg 340 284 487 280 415 355 357 398 471 396 \n"   
    def clean_unregular_landmark_items(self, landmark_path, rest = False):
        if not rest:
            clean_path = landmark_path.replace('.txt', '_clean.txt')
        else:
             clean_path = landmark_path.replace('.txt', '_unregular.txt')
        
        f = open(clean_path, 'w')
        data = utility.read_file(landmark_path);
        for index , elem in enumerate(data):
            elem_num = len(elem.split(' '))
            
            if elem.find('\n') < 0:
                elem += '\n'
             
            if not rest:
                #landmark elem should be 11
                if elem_num == 12:
                    f.write(elem);
            else:
                if elem_num != 12:
                    f.write(elem);
            utility.show_process_percentage(index, len(data)-1, 500)
        f.close()
        
    def clean_list_certain_class_number_label(self, select_num):
        
        dst_path = self.input_folder_path.replace('.txt', '_GE_{}_label.txt'.format(select_num))
        f = open(dst_path, 'w')
        
        data = utility.read_file(self.input_folder_path)
        list_container = []
        class_num = 0
        for index, elem in enumerate(data):
            if len(list_container) == 0:
                list_container.append(elem.split(' ')[0])
            else:
                current_prefix, current_name = utility.get_basename_parent_path(elem.split(' ')[0])
                last_prefix, last_name = utility.get_basename_parent_path(list_container[-1])
                #print(current_prefix, last_prefix)
                
                if current_prefix == last_prefix:
                    list_container.append(elem.split(' ')[0])
                else:
                    if len(list_container) >= select_num  :
                        for line in  list_container:
                            f.write('{} {}\n'.format(line, class_num))
                        class_num +=1
                    list_container = []
                    list_container.append(elem.split(' ')[0])
                    
            utility.show_process_percentage(index, len(data)-1, 1000)
                    
                         
                
        
        
                    
                
            
    
                   
            
        
        