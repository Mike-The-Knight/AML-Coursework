import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


def find_and_display_examples(image_dir, annotation_dir, class_names, output_dir):
    # Initialize a dictionary to store first example of each class
    first_examples = {name: None for name in class_names}

    # Ensure the visualisation directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over annotation files to find the first example of each class
    for filename in os.listdir(annotation_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(annotation_dir, filename), 'r') as file:
                lines = file.readlines()
            for line in lines:
                class_id, x_center, y_center, width, height = map(float, line.split())
                class_name = class_names[int(class_id)]
                if first_examples[class_name] is None:
                    first_examples[class_name] = (filename.replace('.txt', '.jpg'), line)
                    if all(first_examples.values()):  # Stop if we have found an example for each class
                        break
        if all(first_examples.values()):  # Check again in case the last file completed the set
            break
    
    # Display the found examples
    for class_name, (image_name, line) in first_examples.items():
        if image_name:
            image_path = os.path.join(image_dir, image_name)
            image = Image.open(image_path).convert("RGB")
            fig, ax = plt.subplots(1)
            ax.imshow(image)
            x_center, y_center, width, height = map(float, line.split()[1:])
            x = (x_center - width / 2) * image.width
            y = (y_center - height / 2) * image.height
            width = width * image.width
            height = height * image.height
            rect = patches.Rectangle((x, y), width, height, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            plt.title(class_name)
            # Save the figure
            save_path = os.path.join(output_dir, f"{class_name}.png")
            plt.savefig(save_path)
            plt.close()

# Define the directory the images and labels are stored, then display them
image_directory = 'datasets/dataset/train/images'
annotation_directory = 'datasets/dataset/train/labels'
visualisation_directory = 'visualisation'

class_names = ['A10', 'A400M', 'AG600', 'AV8B', 'B1', 'B2', 'B52', 'Be200', 'C130', 'C17', 'C2', 'C5', 'E2', 'E7', 'EF2000', 'F117', 'F14', 'F15', 'F16', 'F18', 'F22', 'F35', 'F4', 'J10', 'J20', 'JAS39', 'KC135', 'MQ9', 'Mig31', 'Mirage2000', 'P3', 'RQ4', 'Rafale', 'SR71', 'Su24', 'Su25', 'Su34', 'Su57', 'Tornado', 'Tu160', 'Tu95', 'U2', 'US2', 'V22', 'Vulcan', 'XB70', 'YF23']
find_and_display_examples(image_directory, annotation_directory, class_names, visualisation_directory)
