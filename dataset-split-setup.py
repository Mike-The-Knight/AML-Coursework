import os
import shutil
from sklearn.model_selection import train_test_split

# Define the paths to the dataset
source_images = 'archive/images/'
source_labels = 'archive/labels/'
dataset_base = 'datasets/dataset/'

# List of all images
all_images = [f for f in os.listdir(source_images) if f.endswith('.jpg')]

# THIS WAS USED FOR THE INITIAL EXPERIMENTS AND WE COMMENTED IT OUT AFTER TO USE THE FULL DATASET FOR A FULL RUN
# Downsample to only use 20% of the images
#_, sampled_images = train_test_split(all_images, test_size=0.2, random_state=42)

# Split the downsampled dataset between test, train and validation
train_images, test_images = train_test_split(all_images, test_size=0.1, random_state=42)  # 10% for testing
train_images, val_images = train_test_split(train_images, test_size=1/9, random_state=42)  # 10% for validation

# Ensure target directories exist
def ensure_dirs(paths):
    for path in paths:
        os.makedirs(path, exist_ok=True)

# Make sure each directory is there before we move images and labels over
ensure_dirs([
    dataset_base + 'train/images', dataset_base + 'train/labels',
    dataset_base + 'val/images', dataset_base + 'val/labels',
    dataset_base + 'test/images', dataset_base + 'test/labels'
])

# Move files into the directories for each split
def move_files(files, split):
    for file in files:
        shutil.move(source_images + file, dataset_base + f'{split}/images/{file}')
        label_file = file.replace('.jpg', '.txt')
        shutil.move(source_labels + label_file, dataset_base + f'{split}/labels/{label_file}')

move_files(train_images, 'train')
move_files(val_images, 'val')
move_files(test_images, 'test')
