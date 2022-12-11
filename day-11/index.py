import os
import sys
import numpy as np
import array
from collections import defaultdict
import math
import json

def run_first_problem():
            
    file_lines = file_to_array("day-11/day-11.txt")

    test_monkey_obj = {
        0: {
            "starting_items": [79, 98], #worry level for each item in inspection order
            "operation": "* 19",
            "test_divisible": 23,
            "if_true_throw": 2,
            "if_false_throw": 3,
            "monkey_business": 0
        },
        1: {
            "starting_items": [54, 65, 75, 74],
            "operation": "+ 6",
            "test_divisible": 19,
            "if_true_throw": 2,
            "if_false_throw": 0,
            "monkey_business": 0
        },
        2: {
            "starting_items": [79, 60, 97],
            "operation": "* old",
            "test_divisible": 13,
            "if_true_throw": 1,
            "if_false_throw": 3,
            "monkey_business": 0
        },
        3: {
            "starting_items": [74],
            "operation": "+ 3",
            "test_divisible": 17,
            "if_true_throw": 0,
            "if_false_throw": 1,
            "monkey_business": 0
        },
    }
    
    test_monkey_obj = {
        0: {
            "starting_items": [92, 73, 86, 83, 65, 51, 55, 93],
            "operation": "* 5",
            "test_divisible": 11,
            "if_true_throw": 3,
            "if_false_throw": 4,
            "monkey_business": 0
        },
        1: {
            "starting_items": [99, 67, 62, 61, 59, 98],
            "operation": "* old",
            "test_divisible": 2,
            "if_true_throw": 6,
            "if_false_throw": 7,
            "monkey_business": 0
        },
        2: {
            "starting_items": [81, 89, 56, 61, 99],
            "operation": "* 7",
            "test_divisible": 5,
            "if_true_throw": 1,
            "if_false_throw": 5,
            "monkey_business": 0
        },
        3: {
            "starting_items": [97, 74, 68],
            "operation": "+ 1",
            "test_divisible": 17,
            "if_true_throw": 2,
            "if_false_throw": 5,
            "monkey_business": 0
        },
        4: {
            "starting_items": [78, 73],
            "operation": "+ 3",
            "test_divisible": 19,
            "if_true_throw": 2,
            "if_false_throw": 3,
            "monkey_business": 0
        },
        5: {
            "starting_items": [50],
            "operation": "+ 5",
            "test_divisible": 7,
            "if_true_throw": 1,
            "if_false_throw": 6,
            "monkey_business": 0
        },
        6: {
            "starting_items": [95, 88, 53, 75],
            "operation": "+ 8",
            "test_divisible": 3,
            "if_true_throw": 0,
            "if_false_throw": 7,
            "monkey_business": 0
        },
        7: {
            "starting_items": [50, 77, 98, 85, 94, 56, 89],
            "operation": "+ 2",
            "test_divisible": 13,
            "if_true_throw": 4,
            "if_false_throw": 0,
            "monkey_business": 0
        },
    }
    
    # find level of monkey business after 20 rounds
    for round in range(0, 20):
        
        for monkey in range(0, len(test_monkey_obj)):
            for item in test_monkey_obj[monkey]["starting_items"]:
                test_monkey_obj[monkey]["monkey_business"] += 1
                operation = test_monkey_obj[monkey]["operation"]
                new_worry_level = item
                
                if "old" in operation:
                    new_worry_level = item * item
                else:
                    operation_number = int(operation.split(" ")[1])
                    if operation.split(" ")[0] == "+":
                        new_worry_level = item + operation_number
                    if operation.split(" ")[0] == "-":
                        new_worry_level = item - operation_number
                    if operation.split(" ")[0] == "*":
                        new_worry_level = item * operation_number
                    
                new_worry_level = math.floor(new_worry_level / 3)
                
                #test if new_worry level is divisible by monkey[""]
                
                #if divisible by
                if not (new_worry_level % int(test_monkey_obj[monkey]["test_divisible"])): #modulo makes 0 if divisible by
                    print(test_monkey_obj)
                    print(test_monkey_obj[throw_monkey_number]["starting_items"])
                    throw_monkey_number = int(test_monkey_obj[monkey]["if_true_throw"])
                    test_monkey_obj[throw_monkey_number]["starting_items"].append(new_worry_level)
                    print(test_monkey_obj[throw_monkey_number]["starting_items"])
                    
                #if not divisible by
                else:
                    throw_monkey_number = int(test_monkey_obj[monkey]["if_false_throw"])
                    test_monkey_obj[throw_monkey_number]["starting_items"].append(new_worry_level)
            
            test_monkey_obj[monkey]["starting_items"] = []
        
        print(test_monkey_obj[monkey]["monkey_business"])
    print(json.dumps(test_monkey_obj))
    
    
    
    
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