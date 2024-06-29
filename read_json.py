"""
Read the contents of the folder /data/data.json and traverse and output the contents corresponding to recover to the file /data/data.txt

"""

import re

input_file_path = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\ema_0.9999_050000.pt.samples\seed110_solverstep10_none.txt'
output_file_path = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\ema_0.9999_050000.pt.samples\data.txt'

# Open the input file and process each line of data
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # delete {"recover": "[CLS]
        line = line.replace('{"recover": "[CLS]', '')  # Delete the specified content
        # Find [SEP] and delete everything after it
        sep_index = line.find('[SEP]')
        if sep_index != -1:
            line = line[:sep_index]  # Keep the content before [SEP]
        output_file.write(line.strip() + '\n')  # Output by line and remove the whitespace at both ends


