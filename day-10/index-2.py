import os
import sys
import numpy as np
import array
from collections import defaultdict


def run_first_problem():
    #array of strings that each elem has 40 characters in
    
    textfile = open("day-10/testfile.txt", "w")
    textfile.write("")
    textfile.close()
    
    textfile = open("day-10/testfile.txt", "a")
    screen_string = "#"
        
    file_lines = file_to_array("day-10/day-10.txt")
    addx_total = 1
    total = 0
    cycle = 1

    for line in file_lines:
        if line == "noop":
            if cycle%40 == 0:
                textfile.write(screen_string+"\n")
                screen_string = ""
            
            cycle += 1
            
            if addx_total == len(screen_string)-1 or addx_total == len(screen_string) or addx_total == len(screen_string)+1:
                screen_string += "#"
            else:
                screen_string += "."
                
            print(str(addx_total) + " : " + str(len(screen_string)))
            print(screen_string)
            
            
                
                
        elif line.split( )[0] == "addx":
            addx_val = int(line.split(" ")[1])

            if cycle%40 == 0:
                textfile.write(screen_string+"\n")
                screen_string = ""
                
            cycle += 1
                
            if addx_total == len(screen_string)-1 or addx_total == len(screen_string) or addx_total == len(screen_string)+1:
                screen_string += "#"
            else:
                screen_string += "."
            
            print(str(addx_total) + " : " + str(len(screen_string)))
            print(screen_string)
            
            if cycle%40 == 0:
                textfile.write(screen_string+"\n")
                screen_string = ""
            
            addx_total += addx_val
            cycle += 1
            
                
            if addx_total == len(screen_string)-1 or addx_total == len(screen_string) or addx_total == len(screen_string)+1:
                screen_string += "#"
            else:
                screen_string += "."
                
            
            
            print(str(addx_total) + " : " + str(len(screen_string)))
            print(screen_string)
                
    textfile.close()
    print(screen_string)

    
    
        
    
    
    
    
    
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