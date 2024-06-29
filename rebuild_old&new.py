"""
Replace the generated code into the source code
"""
import os

# Define smart contract sample location
contract_folder = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\train_1'
data_folder = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\test\dataset_3'

# Get all subfolders under the smart contract sample folder (ie sample name)
sample_folders = [folder for folder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, folder))]

# Traverse each sample folder
for sample_folder in sample_folders:
    # Build the sample folder path
    sample_path = os.path.join(data_folder, sample_folder)
    # Get vulnerability type subfolder
    vulnerability_folders = [folder for folder in os.listdir(sample_path) if
                             os.path.isdir(os.path.join(sample_path, folder))]

    # Traverse vulnerability type subfolders
    for vulnerability_folder in vulnerability_folders:
        # Build the path of the vulnerability type subfolder
        vuln_path = os.path.join(sample_path, vulnerability_folder)
        # Get all txt files
        txt_files = [file for file in os.listdir(vuln_path) if file.endswith('.txt')]

        # Traverse txt files
        for txt_file in txt_files:
            # Extract start and end information
            start_end = os.path.splitext(txt_file)[0].split('-')
            start = int(start_end[0])
            end = int(start_end[1]) + 1

            # Construct the path of the txt file
            txt_path = os.path.join(vuln_path, txt_file)

            # Read the contents of the txt file
            with open(txt_path, 'r', encoding='utf-8') as txt:
                lines = txt.readlines()

            # Build the path of the smart contract sample file
            contract_path = os.path.join(contract_folder, sample_folder + '.sol')

            # Read the content of the smart contract sample file
            with open(contract_path, 'r', encoding='utf-8') as contract:
                contract_lines = contract.readlines()

            # Replace the corresponding line content in the smart contract sample
            replaced_lines = end - start
            lines_count = len(lines)
            if replaced_lines > lines_count:
                lines.extend(['\n'] * (replaced_lines - lines_count))
            elif replaced_lines < lines_count:
                lines = lines[:replaced_lines]

            # Replace the corresponding line content in the smart contract sample and keep the original number of lines
            for i in range(replaced_lines):
                try:
                    contract_lines[start - 1 + i] = lines[i].rstrip('\n') + '\n'
                except IndexError:
                    print(f"Error: Index out of range in file {contract_path}")
                    break

            # Write the updated content back to the smart contract sample file
            with open(contract_path, 'w', encoding='utf-8') as contract:
                contract.writelines(contract_lines)

            # Display the name of the replaced smart contract sample and the number of replaced lines
            print(f"Replace smart contract sample：{contract_path}，Replace Lines：{replaced_lines},{start}-{end - 1}")
