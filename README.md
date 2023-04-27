## Extractor

This project is a Python script with purpose to extract the contents of zip files within a specified directory and its subdirectories. 

To use this script, you need to specify the root directory where you want to extract zip files. The script will then walk through the directory and its subdirectories, searching for any files with the `.zip` extension. When it finds a zip file, it will extract its contents to the same location as the zip file itself. The script uses the `os` and `zipfile` libraries to achieve this functionality.

#### Usage

To use this script, simply replace `"path_to_folder_root"` with the full path to the root directory you want to search for zip files. Then run the script in a Python environment. The script will output the name of each zip file it extracts and the location where it extracted it to.

It's worth noting that this script will extract the contents of the zip files to the same location as the zip files themselves. If you want to extract the contents to a different location, you will need to modify the script accordingly.

#### Requirements

This script requires Python 3 and the `os` and `zipfile` libraries. These libraries should come pre-installed with most Python distributions.
