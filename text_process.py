# -*- coding: utf-8 -*-
"""
Spyder Editor
use to process text file
This is a temporary script file.
"""


import utility

class TextProcess:
    
    def __init__(self, input_path, output_path):
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
            
    
