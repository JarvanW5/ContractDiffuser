"""
Delete Comments
"""

import os
import re


def remove_comments(file_path):
    # Reading file contents
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            content = file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()

    # Delete single-line comments (comments starting with # and //)
    content = re.sub(r'#.*', '', content)
    content = re.sub(r'\/\/.*', '', content)

    # Deleting multi-line comments
    content = re.sub(r'\/\*.*?\*\/', '', content, flags=re.DOTALL)

    # Remove Blank Lines
    content = '\n'.join(line for line in content.splitlines() if line.strip())

    return content


def process_files_in_folder(folder_path):
    # Traverse folders
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.sol'):
                file_path = os.path.join(root, file_name)

                # Read file contents and process them
                content_without_comments = remove_comments(file_path)

                # Construct a new file path, keep the original file name and add the suffix "_new" and the number of content lines
                # new_file_name = os.path.splitext(file_name)[0] + "_" + repr(
                #     content_without_comments.count('\n') + 1) + ".txt"
                new_file_name = os.path.splitext(file_name)[0] + ".sol"
                new_file_path = os.path.join(root, new_file_name)

                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(content_without_comments)


if __name__ == "__main__":
    folder_path = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\clear\RE'
    process_files_in_folder(folder_path)
