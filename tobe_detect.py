"""
Save the data set in the format required by detection

"""

import os
import json


folder_path = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\clear\RE'
output_file = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\clear\RE\data.jsonl'


contract_data_list = []


global_idx = 0


for root, _, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".sol"):

            address = os.path.splitext(filename)[0]
            sol_file_path = os.path.join(root, filename)
            with open(sol_file_path, 'r', encoding='utf-8') as sol_file:
                sol_content = sol_file.read()
            sol_content = sol_content.replace('\\n', '\n')

            contract_data = {
                # "contract": sol_content,
                "code": sol_content,
                "idx": f"{global_idx}",
                # "address": address
                "lable": 1
            }
            contract_data_list.append(contract_data)
            global_idx += 1

with open(output_file, 'w', encoding='utf-8') as json_output:
    for contract_data in contract_data_list:
        json_output.write(json.dumps(contract_data, ensure_ascii=False) + '\n')

print("The .sol file contents have been saved to", output_file)
