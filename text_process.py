# -*- coding: utf-8 -*-
"""
Spyder Editor
use to process text file
This is a temporary script file.
"""


import utility
import os

class TextProcess:
    
    def __init__(self, input_path = "", output_path = ""):
        self.input_path = input_path
        self.output_path = output_path
        
        
#if find = True then   if line.find(select_item) >=0, save find result  [defalut]
#if find = False then   if line.find(select_item) < 0, save result not find
    def selected_certain_part_from_landmark_file(self, select_item, find = True):
        
        f = open(self.output_path, 'w')        
        data = utility.read_file(self.input_path)
        
        for index, line in enumerate(data):
            
            if find:
                if line.find(select_item) >=0:
                    f.write('{}\n'.format(line))
            else:
                if line.find(select_item) < 0:
                    f.write('{}\n'.format(line))
            utility.show_process_percentage(index, len(data)-1, 500)
            
    
    def combine_landmarks_sort(self, add_landmark_path):
        
        origin_landmarks = {elem.split('_landmarks.txt')[0]: elem for elem in os.listdir(self.input_path) if elem.endswith('.txt')}
        add_landmarks = {elem.split('_noface')[0]: elem for elem in os.listdir(add_landmark_path) if elem.endswith('.txt')}
        utility.create_dir(self.output_path)
        
        for key in add_landmarks.keys():
                    if key not in origin_landmarks.keys():
                        print("{} is not exists in original list".format(key))
                        continue
                    add_landmark_file_path = "{}/{}".format(add_landmark_path, add_landmarks[key])
                    origin_landmarks_file_path = "{}/{}".format(self.input_path, origin_landmarks[key])
                    origin_data = utility.read_file(origin_landmarks_file_path)
                    add_data = utility.read_file(add_landmark_file_path)
                    origin_data+=add_data
                    origin_data = sorted(origin_data)
                    
                    #print(key, add_landmarks[key],  origin_landmarks[key])
                    
                    dst_combine_landmark_path = '{}/{}_add_landmarks.txt'.format(self.output_path, key)
                    utility.write_into_file(origin_data, dst_combine_landmark_path)
                    
    def select_face_recognition_result(self, possbility):
        
        dst_result_path = self.input_path.replace('.txt', '_correct_possi{}_select.txt'.format(possbility))
        f = open(dst_result_path, 'w')
        
        data = utility.read_file(self.input_path)
        for index, elem in enumerate(data):
            true_result = float(elem.split(' ')[2])
            true_label = elem.split(' ')[1]
            prefict_label = elem.split(' ')[3]
            if true_label == prefict_label and true_result >=possbility:
                if not elem.endswith('\n'):
                        elem += '\n'
                f.write(elem)
            utility.show_process_percentage(index, len(data)-1, 1000)
        
        
        