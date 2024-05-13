# Move all the images in the dataset into their own folder 
import os
import shutil

# original folder and new folder file paths
original_folder = 'archive/dataset'
new_folder = 'archive/images'

# Make sure the new images folder exists
os.makedirs(new_folder, exist_ok=True)

# Iterate over all files in the source folder
for filename in os.listdir(original_folder):
    
    # Check if the file is a .jpg file
    if filename.endswith('.jpg'):
        
        # Construct full file path
        source_path = os.path.join(original_folder, filename)
        destination_path = os.path.join(new_folder, filename)
        
        # Move the .jpg file to the destination folder
        shutil.move(source_path, destination_path)
