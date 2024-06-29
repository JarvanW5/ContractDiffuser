"""
Read the name of the .sol file in the folder

"""
import os
import csv

# Specify the folder path and output file path
folder_path = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\dataset_folder'
output_file = '/Diffuse/contracts/data_name.csv'

# List to store file names
file_names = []

# Recursively traverse the folder and find all .sol files
for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".sol"):
            # Extract the part before .sol in the file name
            name_without_extension = os.path.splitext(filename)[0]
            file_names.append(name_without_extension)

# Write the file name to a CSV file and print it
with open(output_file, 'w', newline='') as csv_output:
    csv_writer = csv.writer(csv_output)

    # Write the file name
    csv_writer.writerows([[name] for name in file_names])

print("File name saved to", output_file)

# Print file name and number
print("File name and number:")
for name, count in zip(set(file_names), [file_names.count(name) for name in set(file_names)]):
    print(f"{name}: {count} Number")
