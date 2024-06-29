import os
import shutil

slither_data_path = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\datatest3\\newfolder'
vulnerability_path = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\vulnerability_new'
new_folder_path = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\datatest3\\new'

# Get the name of the bottom-level subfolder in slither_data
lowest_level_dirs = []
for root, dirs, files in os.walk(slither_data_path):
    for dir in dirs:
        current_path = os.path.join(root, dir)
        sub_dirs = os.listdir(current_path)
        if not any(os.path.isdir(os.path.join(current_path, d)) for d in sub_dirs):
            lowest_level_dirs.append(current_path)

# Get the name of the bottom-level subfolder in vulnerability
vul_lowest_level_dirs = []
for root, dirs, files in os.walk(vulnerability_path):
    for dir in dirs:
        current_path = os.path.join(root, dir)
        sub_dirs = os.listdir(current_path)
        if not any(os.path.isdir(os.path.join(current_path, d)) for d in sub_dirs):
            vul_lowest_level_dirs.append(current_path)

# Find matching folders and copy to new folder
matching_folders = set()
for slither_dir in lowest_level_dirs:
    slither_dir_name = os.path.basename(slither_dir)
    if any(slither_dir_name == os.path.basename(vul_dir) for vul_dir in vul_lowest_level_dirs):
        parent_folder = os.path.basename(os.path.dirname(slither_dir))
        matching_folders.add(parent_folder)

        # Build the copied path
        destination_folder = os.path.join(new_folder_path, parent_folder)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        else:
            # If the folder already exists, add a sequence number
            count = 1
            while True:
                new_folder_name = f"{parent_folder}_{count}"
                new_destination = os.path.join(new_folder_path, new_folder_name)
                if not os.path.exists(new_destination):
                    destination_folder = new_destination
                    os.makedirs(destination_folder)
                    break
                count += 1

        # Copy a folder and its contents
        try:
            shutil.copytree(slither_dir, destination_folder, dirs_exist_ok=True)
        except FileExistsError:
            pass

# Output the number of matching folders
matching_folders_count = len(matching_folders)
print(f"Number of matching folders found in slither_data: {matching_folders_count}")