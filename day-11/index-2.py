import os
import sys
import numpy as np
import array
from collections import defaultdict
import math
import json
import threading
import concurrent.futures
import requests
import time
import multiprocessing.dummy as mp 
import multiprocessing
from itertools import product

test_monkey_obj = {
    0: {
        "starting_items": [79, 98], 
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

monkey_obj = {
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


def run_concurrently(monkey, item):
    test_monkey_obj[monkey]["monkey_business"] += 1
    operation = test_monkey_obj[monkey]["operation"]
    new_worry_level = 0
    
    if "old" in operation:
        new_worry_level = item ** 2
    else:
        operation_array = operation.split(" ")
        
        operation_char = operation_array[0]
        operation_number = int(operation_array[1])
        if operation_char == "+":
            new_worry_level = item + operation_number
        if operation_char == "-":
            new_worry_level = item - operation_number
        if operation_char == "*":
            new_worry_level = item * operation_number
        
    new_worry_level = math.floor(new_worry_level / 3)

    #if divisible by
    if not (new_worry_level % int(test_monkey_obj[monkey]["test_divisible"])):
        throw_monkey_number = int(test_monkey_obj[monkey]["if_true_throw"])
        test_monkey_obj[throw_monkey_number]["starting_items"].append(new_worry_level)
        
    #if not divisible by
    else:
        throw_monkey_number = int(test_monkey_obj[monkey]["if_false_throw"])
        test_monkey_obj[throw_monkey_number]["starting_items"].append(new_worry_level)



def run_first_problem():
    
    
    monkey_num = len(test_monkey_obj)
    
    # find level of monkey business after 20 rounds
    for round in range(0, 20):
        print(round)
        for monkey in range(0, monkey_num):
            for item in test_monkey_obj[monkey]["starting_items"]:
                pool = multiprocessing.Pool(4)
                out1, out2, out3 = zip(*pool.map(run_concurrently, item, monkey, item))
                
                # run_concurrently(monkey, item)

            test_monkey_obj[monkey]["starting_items"] = []
        
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