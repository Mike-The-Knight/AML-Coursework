import os
import shutil
from sklearn.model_selection import train_test_split

# Define your paths
source_images = 'archive/images/'
source_labels = 'archive/labels/'
dataset_base = 'dataset/'

# List of all images
images = [f for f in os.listdir(source_images) if f.endswith('.jpg')]

# Split the dataset between test, train and validation
train_images, test_images = train_test_split(images, test_size=0.1, random_state=42)  # Here, 10% for testing
train_images, val_images = train_test_split(train_images, test_size=1/9, random_state=42)  # Here, 10% for validation

# Move files into the directories for each split
def move_files(files, split):
    for file in files:
        shutil.move(source_images + file, dataset_base + f'{split}/images/{file}')
        label_file = file.replace('.jpg', '.txt')
        shutil.move(source_labels + label_file, dataset_base + f'{split}/labels/{label_file}')

move_files(train_images, 'train')
move_files(val_images, 'val')
move_files(test_images, 'test')

