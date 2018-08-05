# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:24:43 2018

@author: vince
"""

import os
import sys
import hashlib

#Assumptions for now
certtype = 'md5'

#Get location of Dropped File to pass to windows CertUtil
droppedFile = sys.argv[1]
print(droppedFile)

#Get Expected MD5 checksum and run windows CertUtil on Dropped File
md5Exp = input("Enter Expected MD5 Checksum: ")

#Load File for hashlib - Will hash string if left alone
with open(droppedFile, 'rb') as file_handle:    
    file_contents = file_handle.read()
    md5Act = hashlib.md5(file_contents).hexdigest().upper()
    print('Actual '+certtype+' hash is: '+md5Act)

#Compare and Exit or ask user to delete
if md5Exp == md5Act:
    print('File matches '+certtype+' checksum.')
else:
    print('File does NOT match '+certtype+' checksum.')
    if input('Delete[y/n]: ') == 'y':
        os.remove(droppedFile)
        print(droppedFile+' deleted')

input('Hit any key to exit')
