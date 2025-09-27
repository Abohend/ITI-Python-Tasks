# 6) Random Data Generator
#    - Ask user how many random numbers to generate.
#    - Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - Print total count and average of the generated numbers.

import os
import random


def GenerateData():
    # Ask user how many random numbers to generate.
    lS = input("How many nums to generate: ")
    while not lS.isdigit():
        print("Enter a valid number.")
        lS = input("How many nums to generate: ")

    l = int(lS)
#    Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - 
    total = 0
    fileName = "random_numbers.csv"
    with open(fileName, "w") as file:
        file.write("inded, value\n")
        for i in range(1, l + 1):
            num = random.randint(1,100)
            total += num
            file.write(f"{i}, {num}\n")
    
    #Print total count and average of the generated numbers.
    print(f"total: {total}")
    print(f"average: {total/l}")