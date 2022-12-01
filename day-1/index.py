import os
import sys
import numpy as np


def run_first_problem():
    print("first problem")
    file_lines = file_to_array("day-1/day-1.txt")
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()