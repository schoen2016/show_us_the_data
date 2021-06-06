'''
    Filename: paddedPattern.py
    Author: Alexander Schoen
    Version: 1.0
    Date: 5/30/2021
    Description: Creates a list of substring containing a pattern.  The substrings are padded with a specified number of words around the pattern.
'''

import re
from sys import argv

def buildPattern(sub_str, pad_length):
    pattern = '('+sub_str+')'
    for i in range(0,pad_length):
        pattern = '(\w*)\W*'+pattern+'\W*(\w*)'
    
    return pattern

def find(sub_str, str1, pad_length,):
    arr = list()
    pattern = buildPattern(sub_str,pad_length)
    
    for i in re.findall(pattern, str1, re.I):
        arr.append(" ".join([x for x in i if x != ""]))
    
    return arr

if __name__=='__main__':
    print(find(argv[1], argv[2], int(argv[3])))
