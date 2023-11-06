import os

# Directory containing your text files
directory_path = '/path/to/your/directory'

# List all files in the directory
file_list = os.listdir(directory_path)

# Iterate through each file
for filename in file_list:
    if filename.endswith('.txt'):  # Check if it's a text file
        with open(os.path.join(directory_path, filename), 'r') as file:
            file_contents = file.read()
            if '1' in file_contents or '2' in file_contents:
                print(f"File {filename} contains a 1 or a 2.")
