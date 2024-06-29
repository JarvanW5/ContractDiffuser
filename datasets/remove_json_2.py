"""
Traverse the folder /data/newsource and move the empty folders with "v0" in their names to the folder /data/null.
Also move the .sol files with the same name as the empty folders.
"""

import os
import shutil

source_folder = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\slither_folder'
null_folder = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\nulljson1'

for root, dirs, files in os.walk(source_folder, topdown=False):
    for dir_name in dirs:
        if 'v0' in dir_name:
            dir_path = os.path.join(root, dir_name)
            sol_file = os.path.join(root, dir_name + '.sol')
            if not os.listdir(dir_path) and os.path.exists(sol_file):
                # Move empty folders and corresponding .sol files
                shutil.move(dir_path, os.path.join(null_folder, dir_name))
                shutil.move(sol_file, os.path.join(null_folder, dir_name + '.sol'))

print("finished!")
