import os
import zipfile

# Set the root directory to search
root_dir = "path_to_folder_root"

# Walk through the directory and its subdirectories
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file is a zip file
        if file.endswith(".zip"):
            # Get the full path to the zip file
            zip_path = os.path.join(subdir, file)
            # Extract the contents of the zip file to the same location
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(subdir)
                print(f"Extracted {file} to {subdir}")
