# Define all the aircraft classes
aircraft_classes = {
    'A10': 0, 'A400M': 1, 'AG600': 2, 'AV8B': 3, 'B1': 4, 'B2': 5, 'B52': 6, 'Be200': 7,
    'C130': 8, 'C17': 9, 'C2': 10, 'C5': 11, 'E2': 12, 'E7': 13, 'EF2000': 14, 'F117': 15,
    'F14': 16, 'F15': 17, 'F16': 18, 'F18': 19, 'F22': 20, 'F35': 21, 'F4': 22, 'J10': 23,
    'J20': 24, 'JAS39': 25, 'KC135': 26, 'MQ9': 27, 'Mig31': 28, 'Mirage2000': 29, 'P3': 30,
    'RQ4': 31, 'Rafale': 32, 'SR71': 33, 'Su24': 34, 'Su25': 35, 'Su34': 36, 'Su57': 37,
    'Tornado': 38, 'Tu160': 39, 'Tu95': 40, 'U2': 41, 'US2': 42, 'V22': 43, 'Vulcan': 44,
    'XB70': 45, 'YF23': 46
}

import pandas as pd
import os

# Old labels and new labels file paths
csv_dir = 'archive/dataset'
labels_dir = 'archive/labels'

# Make sure the labels directory exists
os.makedirs(labels_dir, exist_ok=True)

# Iterate over all files in the source folder
for csv_file in os.listdir(csv_dir):
    if csv_file.endswith('.csv'):
        # Load the csv file with all the labels
        df = pd.read_csv(os.path.join(csv_dir, csv_file))
        yolo_data = {}
        # Iterate over all the rows in the dataframe
        for _, row in df.iterrows():
            filename = row['filename'] + '.txt'
            width, height = row['width'], row['height']
            class_name = row['class']  # This is the aircraft type name
            cls = aircraft_classes[class_name]  # Convert to class ID
            xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
            
            # Convert to YOLO format
            x_center_normalized = ((xmin + xmax) / 2) / width
            y_center_normalized = ((ymin + ymax) / 2) / height
            width_normalized = (xmax - xmin) / width
            height_normalized = (ymax - ymin) / height
            
            # Append to the yolo_data dictionary
            yolo_format = f"{cls} {x_center_normalized} {y_center_normalized} {width_normalized} {height_normalized}"
            
            if filename in yolo_data:
                yolo_data[filename].append(yolo_format)
            else:
                yolo_data[filename] = [yolo_format]
        
        # Write it to a new .txt file with the YOLO label format
        for filename, annotations in yolo_data.items():
            with open(os.path.join(labels_dir, filename), 'w') as file:
                file.write('\n'.join(annotations))

