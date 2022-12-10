import os
import sys
import numpy as np
import array
from collections import defaultdict


def run_first_problem():
    #array of strings that each elem has 40 characters in
    
    screen_string = ""
        
    file_lines = file_to_array("day-10/day-9.txt")
    addx_total = 1
    total = 0
    cycle = 1

    for line in file_lines:
        if line == "noop":
            cycle += 1
            
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                total += addx_total * cycle
                print(cycle)
                print(addx_total)
                print(total)
                
                
        elif line.split( )[0] == "addx":
            addx_val = int(line.split(" ")[1])
            
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                total += addx_total * cycle
                print("first")
                print(cycle)
                print(addx_total)
                print(addx_total * cycle)
                print(total)
            
            
            addx_total += addx_val
            cycle += 1
            
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                total += addx_total * cycle
                print("second")
                print(cycle)
                print(addx_total)
                print(addx_total * cycle)
                print(total)
                
            
                        
    print(total)
    
    
        
    
    
    
    
    
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