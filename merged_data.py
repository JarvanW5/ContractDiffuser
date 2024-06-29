import os
import json

# Integrate data into the input requirements of the diffusion model
# Vulnerability folder path
vulnerability_folder = "D:\\JarvanW\\workplace\\python\\Diffusion-LM-main\\Diffuse\\contracts\\vulnerability_new"
#Store the integrated data
result_data = []
# Counter initialization
file_count = 0

# Traverse the subfolders in slither_folder
for root, dirs, files in os.walk(
        r"D:\JarvanW\workplace\python\Diffusion-LM-main\test\dataset_3"):
    for folder in dirs:
        folder_path = os.path.join(root, folder)

        # Get the folder name of the vulnerability type
        vulnerability_type = folder
        vulnerability_folder_path = os.path.join(vulnerability_folder, vulnerability_type)

        # Check if the vulnerability folder exists
        if os.path.exists(vulnerability_folder_path):
            # Read the txt file content of the vulnerability type
            with open(os.path.join(vulnerability_folder_path, f"{vulnerability_type}.txt"), "r", encoding='utf-8') as f:
                vulnerability_content = f.read()

            # Traverse the txt files in the subfolders
            for txt_file in os.listdir(folder_path):
                if txt_file.endswith(".txt"):
                    txt_file_path = os.path.join(folder_path, txt_file)

                    # Read the contents of the txt file in the subfolder
                    with open(txt_file_path, "r", encoding='utf-8') as f:
                        txt_content = f.read()

                    # Integrate data into JSON format
                    data = {"src": vulnerability_content, "trg": txt_content}
                    result_data.append(data)

# Save the integrated data to a JSON file, with each data in one line
with open(r"D:\JarvanW\workplace\python\Diffusion-LM-main\test\test1.jsonl",
          "w") as json_file:
    for data in result_data:
        json_file.write(json.dumps(data) + "\n")

print("Data integration completed!")
