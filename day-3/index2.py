import os
import sys
import numpy as np
import array

def run_first_problem():
    file_lines = file_to_array("day-3/day-3.txt")
    
    for line in file_lines:
        print(line)
        
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()