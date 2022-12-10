import os
import sys
import numpy as np
import array
from collections import defaultdict

path = []
folders = defaultdict(int)

# TODO something wrong with diaganols
def more_than_one_away(current_positions):
    #TODO work with negatives
    if abs(current_positions["h"]["x"] - current_positions["t"]["x"]) > 1:
        return True
    
    if abs(current_positions["h"]["y"] - current_positions["t"]["y"]) > 1:
        return True
    
    return False

def run_first_problem():
    file_lines = file_to_array("day-9/day-9.txt")
    total_count = 0
    
    #x and y coordinates
    past_position_array = ["0,0"]
    head_position_array = ["0,0"]
        
    current_positions = {
        "h": {
            "x": 0,
            "y": 0
        },
        "t": {
            "x": 0,
            "y": 0
        }
    }
    
    for line in file_lines:
        line = line.split(" ")
        for step in range(0, int(line[1])):
            previous_head_coord ={
                "x": current_positions["h"]["x"],
                "y": current_positions["h"]["y"]
            } 
            
            if line[0] == "L":
                current_positions["h"]["x"] -= 1
                    
            elif line[0] == "R":
                current_positions["h"]["x"] += 1
                
            elif line[0] == "D":
                current_positions["h"]["y"] -= 1
                
            elif line[0] == "U":
                current_positions["h"]["y"] += 1
                
            head_position_array.append(str(current_positions["h"]["x"]) + "," + str(current_positions["h"]["y"]))
                
            if more_than_one_away(current_positions):
                current_positions["t"]["x"] = previous_head_coord["x"]
                current_positions["t"]["y"] = previous_head_coord["y"]
                
                past_move_string = str(current_positions["t"]["x"]) + "," + str(current_positions["t"]["y"])
                
                past_position_array.append(past_move_string)
    
    
    print(past_position_array)
    
    #remove duplicates from array
    unique_array = []
    for i in past_position_array:
        if i not in unique_array:
            unique_array.append(i)
    
    print(len(unique_array))
        
            
    
    
        
    
    
    
    
    
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