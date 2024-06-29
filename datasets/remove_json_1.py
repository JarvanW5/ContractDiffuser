"""
Remove the first contract with incorrect json format

"""

import os
import shutil

# Define the source and destination folders
source_folder = "D:/JarvanW/workplace/python/Diffusion-LM-main/Diffuse/contracts/share_folder/0.8.9"
destination_folder = "D:/JarvanW/workplace/python/Diffusion-LM-main/Diffuse/contracts/new/0.8.9"
keyword = '"language": "Solidity"'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Initialize a counter to keep track of the number of files moved
files_moved_count = 0
files_count = 0

# Traverse through the source folder and process .sol files
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".sol"):
            file_path = os.path.join(root, file)
            files_count += 1

            # Read the content of the .sol file
            with open(file_path, 'r', encoding='utf-8') as sol_file:
                content = sol_file.read()

            # Check if the content contains the specified keyword
            if keyword in content:
                # Move the file to the destination folder
                destination_path = os.path.join(destination_folder, file)
                shutil.move(file_path, destination_path)
                files_moved_count += 1
                print(f"Moved {file} to {destination_path}")

print(f"Total files : {files_count}")
print(f"Total files moved: {files_moved_count}")
