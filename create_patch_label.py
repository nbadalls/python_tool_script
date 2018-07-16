#create patch label

import os
import sys

#create label from list
def create_patch_label_from_list(crop_list):
     
     f = open(crop_list, 'r')
     data = f.read().splitlines()
     f.close()
     
     dst_path = '{}_label.txt'.format(crop_list)
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
   

#travel folder to create image list                            
def create_folder_list2(src_image_folder, prefix_result):

         dst_path = '{}_list.txt'.format(src_image_folder)
         f = open(dst_path, 'w')
         for root_path, folder_path, filenames_path in os.walk(src_image_folder):
                    for index, elem in   enumerate(filenames_path):
                            image_path = '{}/{}'.format(root_path, elem)
                            prefix_name = image_path.split(src_image_folder)[1]
                            save_prefix = '{}{}\n'.format(prefix_result, prefix_name)
                            f.write(save_prefix)
                            sys.stdout.write('{}/{}\r'.format(index, len(filenames_path)-1))
                            sys.stdout.flush()
         f.close()



if __name__ == '__main__':

    #src_image_folder = sys.argv[1]
    #prefix_result = src_image_folder.split('/')[-1]
    #create_folder_list2(src_image_folder, prefix_result)

    crop_list = sys.argv[1]
    create_patch_label_from_list(crop_list)

