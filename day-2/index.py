import os
import sys
import numpy as np
import array

def run_first_problem():
    print("first problem")
    file_lines = file_to_array("day-2/day-2.txt")
    total_points = 0
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # x for Rock, Y for Paper, and Z for Scissors
    for line in file_lines:
        line = line.split(' ')
        
        if(line[0] == "A"):
            if(line[1] == "X"):
                total_points += 0
                total_points += 3
                
            if(line[1] == "Y"):
                total_points += 3
                total_points += 1
            
            if(line[1] == "Z"):
                total_points += 6
                total_points += 2
        
        if(line[0] == "B"):
            if(line[1] == "X"):
                total_points += 0
                total_points += 1
                
            if(line[1] == "Y"):
                total_points += 3
                total_points += 2
            
            if(line[1] == "Z"):
                total_points += 6
                total_points += 3
        
        if(line[0] == "C"):
            if(line[1] == "X"):
                total_points += 0
                total_points += 2
                
            if(line[1] == "Y"):
                total_points += 3
                total_points += 3
            
            if(line[1] == "Z"):
                total_points += 6
                total_points += 1
            
        
        print(total_points)
            
    
    
    
    
def file_to_array(file_name):
    line_array = []
    with open(file_name) as my_file:
        for line in my_file:
            line_array.append(line.strip())
            
    return line_array

if __name__ == '__main__':
    run_first_problem()