import os
import sys
import numpy as np
import array

def run_first_problem():
    print("first problem")
    file_lines = file_to_array("day-1/day-1.txt")
    
    highest_number = 0
    running_add = 0
    total_array = []
    
    for line in file_lines:
        if line == '':
            total_array.append(running_add)
            running_add = 0
        else:
            running_add += int(line)
    
    
    print(sorted(total_array))
            
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()