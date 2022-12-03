import os
import sys
import numpy as np
import array

def run_first_problem():
    file_lines = file_to_array("day-3/day-3.txt")
        
    total_priority = 0
    index = 1
    triple_array = []
    
    for line in file_lines:
        
        if index < 3:
            triple_array.append(line)
            index += 1
        else:
            
            triple_array.append(line)
            print(triple_array)
            a=list(set(triple_array[0])&set(triple_array[1])&set(triple_array[2]))
            print(a)
            
            if a[0].isupper():
                total_priority += ((ord(a[0]) - 64) + 26) 
            else:
                total_priority += (ord(a[0]) - 96) 
                        
            index = 1
            triple_array = []
        
    print(total_priority)
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()