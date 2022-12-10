import os
import sys
import numpy as np
import array
from collections import defaultdict

path = []
folders = defaultdict(int)

def more_than_one_away(x1, y1, x2, y2):
    if abs(x2 - x1) > 1:
        return True
    
    if abs(y2 - y1) > 1:
        return True
    
    return False

def run_first_problem():
    file_lines = file_to_array("day-9/day-9.txt")
    total_count = 0
    
    #x and y coordinates
    tail_position_array = ["0,0"]
    head_position_array = ["0,0"]
        
    current_positions = {
        "h0": {
            "x": 0,
            "y": 0
        },
        "h1": {
            "x": 0,
            "y": 0
        },
        "h2": {
            "x": 0,
            "y": 0
        },
        "h3": {
            "x": 0,
            "y": 0
        },
        "h4": {
            "x": 0,
            "y": 0
        },
        "h5": {
            "x": 0,
            "y": 0
        },
        "h6": {
            "x": 0,
            "y": 0
        },
        "h7": {
            "x": 0,
            "y": 0
        },
        "h8": {
            "x": 0,
            "y": 0
        },
        "h9": {
            "x": 0,
            "y": 0
        },
        "h10": {
            "x": 0,
            "y": 0
        }
    }
    
    for line in file_lines:
        line = line.split(" ")
        for step in range(0, int(line[1])):
            previous_head_coord ={
                "x": current_positions["h9"]["x"],
                "y": current_positions["h9"]["y"]
            } 
            
            if line[0] == "L":
                current_positions["h0"]["x"] -= 1
                    
            elif line[0] == "R":
                current_positions["h0"]["x"] += 1
                
            elif line[0] == "D":
                current_positions["h0"]["y"] -= 1
                
            elif line[0] == "U":
                current_positions["h0"]["y"] += 1
                
            head_position_array.append(str(current_positions["h0"]["x"]) + "," + str(current_positions["h0"]["y"]))
                
            if more_than_one_away(current_positions["h0"]["x"], current_positions["h0"]["y"], current_positions["h1"]["x"], current_positions["h1"]["y"]):
                for segment in range(1, 10):
                    current_positions["h"+str(segment)]["x"] = current_positions["h"+str(segment-1)]["x"]
                    current_positions["h"+str(segment)]["y"] = current_positions["h"+str(segment-1)]["y"]
                    print(segment)
                    if segment == 9:
                        seg_string = str(current_positions["h10"]["x"]) + "," + str(current_positions["h10"]["y"])
                        tail_position_array.append(seg_string)
    
    #remove duplicates from array
    unique_array = []
    for i in tail_position_array:
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