"""
Convert multiple lines of code in the sol file into a single line of code and connect them with "\\n"

"""

import os


def concatenate_lines_in_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.sol'):
                file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, file_name.replace('.sol', '.sol'))

                concatenated_text = ''
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        concatenated_text += line.strip() + '\\n '
                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(concatenated_text)

if __name__ == "__main__":
    folder_path = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\clear\RE'
    concatenate_lines_in_files(folder_path)
