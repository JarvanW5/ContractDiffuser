import csv
import random

"""
Divide the files into training set, validation set, and test set in proportion
"""
input_file = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\0.8.csv'

train_output_file = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\train.txt'
test_output_file = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\test.txt'
valid_output_file = r'D:\JarvanW\workplace\python\Diffusion-LM-main\test\valid.txt'

# %
train_percentage = 0
test_percentage = 100
valid_percentage = 0


data_list = []


with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data_list.append([row[0], row[2]])


random.shuffle(data_list)


total_rows = len(data_list)
train_rows = int(total_rows * (train_percentage / 100))
test_rows = int(total_rows * (test_percentage / 100))
valid_rows = int(total_rows * (valid_percentage / 100))


train_data = data_list[:train_rows]
test_data = data_list[train_rows: train_rows + test_rows]
valid_data = data_list[train_rows + test_rows:]



def write_to_file(data, file_path):
    with open(file_path, 'w', newline='') as output_file:
        for row in data:
            output_file.write('\t'.join(row) + '\n')



write_to_file(train_data, train_output_file)
write_to_file(test_data, test_output_file)
write_to_file(valid_data, valid_output_file)

print(f"train set:({train_percentage}%)、test set:({test_percentage}%)、valid set:({valid_percentage}%)")
