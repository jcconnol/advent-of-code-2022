import os
import sys
import numpy as np
import array
from collections import defaultdict

path = []
folders = defaultdict(int)

def run_first_problem():
    with open('day-7/day-7.txt', 'r') as f:
        for line in f:
            if line[:7] == '$ cd ..':
                path.pop()
            elif line[:4] == '$ cd':
                path.append(line.strip()[5:])
            elif line[0].isdigit():
                size = line.split()
                for i in range(len(path)):
                    folders['/'.join(path[:i + 1])] += int(size[0])
    
    total = 0
    for f in folders.values():
        if f <= 100000:
            total += f
            
    print(total)
    
    total2 = 0
    total_array = []
    for f in folders.values():
        if folders['/'] - f <= 40000000:
            total_array.append(f)
            min([f for f in folders.values() if folders['/'] - f <= 40_000_000])
            
    print(min(total_array))
    
    
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