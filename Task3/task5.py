# 5) OS File Manager
#    - Ask user for a directory path.
#    - Automatically:
#         - Create a folder "backup" inside it if not exists.
#         - Copy all .txt files into "backup".
#         - Print summary: how many files copied.
#    - If directory invalid, retry until correct.

import os
import shutil


def manageFile():
    # Ask user for a directory path.
    dirPath = input("Enter a directory Path: ")
    while not os.path.exists(dirPath):
        print("Path not found!")
        dirPath = input("Enter a directory Path: ")
    
    # Create a folder "backup" inside it if not exists.
    backupFolder = os.path.join(dirPath, "backup")
    os.makedirs(backupFolder, exist_ok=True)

    # Copy all .txt files into "backup".
    copiedCnt = 0
    for fileName in os.listdir(dirPath):
        filePath = os.path.join(dirPath, fileName)
        if os.path.isfile(filePath) and fileName.lower().endswith(".txt"):
            shutil.copy(filePath, backupFolder)
            copiedCnt +=1
    # Print summary: how many files copied.
    print(f"copied {copiedCnt} .txt files.")