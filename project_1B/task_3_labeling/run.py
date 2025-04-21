import os
import shutil
import random

# Configuration
image_folder = 'images'
label_folder = 'labels'
output_folder = 'dataset'
train_ratio = 0.8  # 80% train, 20% val

# Create output directories
for subfolder in ['images/train', 'images/val', 'labels/train', 'labels/val']:
    os.makedirs(os.path.join(output_folder, subfolder), exist_ok=True)

# Get all image filenames
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Shuffle and split
random.shuffle(image_files)
split_index = int(len(image_files) * train_ratio)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

# Helper to copy image and label
def copy_pair(images_list, subset):
    for img_name in images_list:
        # Copy image
        shutil.copy(os.path.join(image_folder, img_name),
                    os.path.join(output_folder, f'images/{subset}', img_name))

        # Copy label with same name but .txt
        label_name = os.path.splitext(img_name)[0] + '.txt'
        label_path = os.path.join(label_folder, label_name)
        if os.path.exists(label_path):
            shutil.copy(label_path,
                        os.path.join(output_folder, f'labels/{subset}', label_name))

# Copy to new folders
copy_pair(train_images, 'train')
copy_pair(val_images, 'val')

print("Dataset split completed successfully.")
