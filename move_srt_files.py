import os
import shutil

# Define source and destination directories
source_folder = r'path'
destination_folder = r'path'

# Ensure destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Iterate over all files and move .srt files
for file_name in files:
    if file_name.endswith('.vtt'):
        # Construct full file paths
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)

        try:
            # Move file to the destination
            shutil.move(source_file, destination_file)
            print(f'Moved: {file_name}')
        except Exception as e:
            print(f'Error moving {file_name}: {e}')

print('All .srt files have been moved.')
