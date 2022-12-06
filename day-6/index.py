import os
import sys
import numpy as np
import array

def run_first_problem():
    file_lines = file_to_array("day-6/day-6.txt")
    total_count = 0
    
    # output index of end of first 4 characters that are all different
    for line in file_lines: 
        unique_index = 13
        for index in range(unique_index, len(line)):
            last_3_chars = line[index-13] + line[index-12] + line[index-11] + line[index-10] + line[index-9] + line[index-8] + line[index-7] + line[index-6] + line[index-5] + line[index-4] + line[index-3] + line[index-2] + line[index-1] + line[index]
            
            
            
            if isUniqueChars(last_3_chars):
                print(last_3_chars)
                print(index)
                break
    
    
    
    
def isUniqueChars(st):
 
    # String length cannot be more than
    # 256.
    if len(st) > 256:
        return False
 
    # Initialize occurrences of all characters
    char_set = [False] * 128
 
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(st)):
 
        # Find ASCII value and check if it
        # exists in set.
        val = ord(st[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True
    
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()