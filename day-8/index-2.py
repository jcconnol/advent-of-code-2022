import os
import sys
import numpy as np
import array
from collections import defaultdict

path = []
folders = defaultdict(int)

def run_first_problem():
    file_lines = file_to_array("day-8/day-8.txt")
    total_count = 0
    
    for line in file_lines:
        print(line)
    
    
    
    print(total_count)
    
    
    
    
    
    
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