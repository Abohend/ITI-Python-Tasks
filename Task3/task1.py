# 1) Math Automation
#    - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.

from math import ceil, floor, nan, pi, sqrt
import os
from task7 import log_time

@log_time
def automateMath():
    fileName = "math_report.txt"
    while True:
        s = input("Enter comma seperated nums: ")
        try:
            nums = [float(num) for num in s.split(",")]
            break
        except:
            print("Invalid comma seperated nums")
    with open(fileName, "w") as file:
        file.write("num: floor, ceil, square root, circle area")
        for num in nums:
            sqr = sqrt(num) if num >=0 else nan
            file.write(f"{num}: {floor(num)}, {ceil(num)}, {sqr}, {pi*num*num}\n")
    if os.path.exists(fileName):
        print("File Contents:")
        with open(fileName, "r") as file:
            print(file.read())
    else:
        print("file not found!")       
    
