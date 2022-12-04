import os
import sys
import numpy as np
import array

def run_first_problem():
    file_lines = file_to_array("day-4/day-4.txt")
    total_count = 0
    for line in file_lines:
        print(line)
        
        elf1 = line.split(',')[0]
        elf2 = line.split(',')[1]
        
        elf1_first = int(elf1.split('-')[0])
        elf1_second = int(elf1.split('-')[1])
        
        elf2_first = int(elf2.split('-')[0])
        elf2_second = int(elf2.split('-')[1])
    
        if elf1_second < elf2_first or elf1_first > elf2_second:
            # total_count += 1
            
            print("yes")
            
        elif elf2_second < elf1_first or elf2_first > elf1_second:
            # total_count += 1
            print("yes")
            
        else:
            total_count += 1
    
    print(total_count)
    
    
    
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()