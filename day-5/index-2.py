import os
import sys
import numpy as np
import array

def run_first_problem():
    file_lines = file_to_array("day-5/day-5.txt")
    total_count = 0
    
    stack_array = [
        "NDMQBPZ",
        "CLZQMDHV",
        "QHRDVFZG",
        "HGDFN",
        "NFQ",
        "DQVZFBT",
        "QMTZDVSH",
        "MGFPNQ",
        "BWRM"
    ]
    
    for line in file_lines:
        print(line)
        line_array = line.split(' ')
        print(line_array)
        
        loop_number = int(line_array[1])
        string_adding = ""

        for index in range(loop_number):
            print(index)
            print(line_array[3])
            removing_string = stack_array[int(line_array[3])-1]
            adding_string = stack_array[int(line_array[5])-1]
            
            letter_to_add = removing_string[-1]
            
            stack_array[int(line_array[3])-1] = removing_string[:len(removing_string)-1]
            
            string_adding = letter_to_add + string_adding
        
        stack_array[int(line_array[5])-1] = stack_array[int(line_array[5])-1] + string_adding
    
    
    print(stack_array)
    
    
    
    
    
    
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()