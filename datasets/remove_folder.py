import os
import shutil

def delete_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            folder_path = os.path.join(root, name)
            shutil.rmtree(folder_path)

if __name__ == '__main__':
    path = 'D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\slither_folder\\0.8\\0.8.9'
    delete_folders(path)
