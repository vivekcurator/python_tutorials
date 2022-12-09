#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:42:27 2022

@author: viveksaini
"""

# import OS module
import os
 
# Get the list of all files and directories
path = "/Users/viveksaini/Desktop/"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)