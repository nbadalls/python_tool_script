# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:31:04 2018

@author: zkx-97
"""
import sys
import os


def read_file(file_path):
    f = open(file_path, 'r')
    data = f.read().splitlines()
    f.close()
    return data
    
def show_process_percentage(index, sum_num, display_gap):
    if index % display_gap == 0:
        percentage = round(float(index) / float(sum_num),2)*100
        sys.stdout.write('{}/{}\t{}%\n'.format(index, sum_num, percentage))
        sys.stdout.flush()
    if index == sum_num:
        sys.stdout.write('{}/{}\t100.0%\n'.format(index, sum_num))
        sys.stdout.flush()
        
def create_dir(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)