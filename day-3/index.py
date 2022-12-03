import os
import sys
import numpy as np
import array

def run_first_problem():
    file_lines = file_to_array("day-3/day-3.txt")
    
    # each line is ruck sack, first half of letters are first compartment, sencond half are second
    # a vs A are different
    
    total_priority = 0
    
    for line in file_lines:
        print(line)
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        
        a=list(set(first_half)&set(second_half))
        
        print(a)
        
        if a[0].isupper():
            total_priority += (ord(a[0]) - 64) + 26
        else:
            total_priority += (ord(a[0]) - 96)
            
    print(total_priority)
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()