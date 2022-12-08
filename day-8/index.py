import os
import sys
import numpy as np
import array
from collections import defaultdict

path = []
folders = defaultdict(int)

def run_first_problem():
    file_lines = file_to_array("day-8/day-8.txt")
    total_count = 0
    tree_array = []
    tree_score_array = []
    
    for line in file_lines:
        tree_array.append(line)
            
    row_index = 0
    column_index = 0
    
    print(tree_array)
    
    for row in tree_array:
        for column in row:
            #This handles the first and last rows
            if row_index == 0 or row_index == (len(tree_array)-1):
                total_count += 1
            elif int(column_index) == 0 or int(column_index) == (len(row)-1):
                total_count += 1
            else:
                current_tree_height = int(row[column_index])
                                
                # check all trees above current row and column
                up_score = 0
                for tree_row_index in reversed(range(0, row_index)):
                    up_score += 1
                    if current_tree_height <= int(tree_array[tree_row_index][column_index]):
                        break
                        
                    
                
                # check all trees below current row and column
                down_score = 0
                for tree_row_index in range(row_index+1, len(tree_array)):
                    down_score += 1
                    if current_tree_height <= int(tree_array[tree_row_index][column_index]):
                        break
                
                    
                
                # check all trees to left of current row and column
                left_score = 0
                for tree_col_index in reversed(range(0, column_index)):
                    left_score += 1
                    if current_tree_height <= int(row[tree_col_index]):
                        break
                
                    
                
                # check all trees to right of current row and column
                right_score = 0
                for tree_col_index in range(column_index+1, len(row)):
                    right_score += 1
                    if current_tree_height <= int(row[tree_col_index]):
                        break
                    
                    
                
                print(str(up_score) + " " + str(left_score) + " " + str(down_score) + " " + str(right_score))
                
                tree_score_array.append(right_score*left_score*up_score*down_score)
                
            column_index += 1
            
        row_index += 1
            
        column_index = 0
        
    tree_score_array.sort()
    print(tree_score_array)
    
    
    
    
    
    
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