import os
import random
import shutil

# =========================================================
# DIRS21 Dataset Split Script for YOLOv8
# =========================================================

# MAIN PROJECT PATH
base_path = r"C:\Users\pqin\OneDrive\Documents\DIRS21_yolov8"

# =========================================================
# DATASET PATHS
# =========================================================

# Folder containing all JPG images
image_folder = os.path.join(
    base_path,
    "DIRS21",
    "DIRS21",
    "DIRS21"
)

# Folder containing YOLO txt labels
label_folder = os.path.join(
    base_path,
    "DIRS21",
    "DIRS21",
    "DIRS21",
    "YOLO_Darknet"
)

# Output dataset folder
output_base = os.path.join(base_path, "dataset")

# =========================================================
# CREATE OUTPUT FOLDERS
# =========================================================

for split in ['train', 'val', 'test']:

    os.makedirs(
        os.path.join(output_base, 'images', split),
        exist_ok=True
    )

    os.makedirs(
        os.path.join(output_base, 'labels', split),
        exist_ok=True
    )

# =========================================================
# GET ALL IMAGE FILES
# =========================================================

images = [
    f for f in os.listdir(image_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
]

print("\n========================================")
print(f"Total images found: {len(images)}")
print("========================================\n")

# Shuffle images randomly
random.shuffle(images)

# =========================================================
# TRAIN / VAL / TEST SPLIT
# =========================================================

train_split = int(0.8 * len(images))
val_split = int(0.9 * len(images))

train_files = images[:train_split]
val_files = images[train_split:val_split]
test_files = images[val_split:]

print(f"Train images: {len(train_files)}")
print(f"Validation images: {len(val_files)}")
print(f"Test images: {len(test_files)}\n")

splits = {
    'train': train_files,
    'val': val_files,
    'test': test_files
}

# =========================================================
# COPY IMAGES + LABELS
# =========================================================

for split_name, file_list in splits.items():

    print(f"\nProcessing {split_name} set...")

    copied_images = 0
    copied_labels = 0
    missing_labels = 0

    for image_file in file_list:

        # SOURCE IMAGE PATH
        src_image = os.path.join(image_folder, image_file)

        # DESTINATION IMAGE PATH
        dst_image = os.path.join(
            output_base,
            'images',
            split_name,
            image_file
        )

        # COPY IMAGE
        shutil.copy2(src_image, dst_image)
        copied_images += 1

        # LABEL FILE NAME
        label_file = os.path.splitext(image_file)[0] + ".txt"

        # SOURCE LABEL PATH
        label_path = os.path.join(label_folder, label_file)

        # DESTINATION LABEL PATH
        dst_label = os.path.join(
            output_base,
            'labels',
            split_name,
            label_file
        )

        # COPY LABEL IF EXISTS
        if os.path.exists(label_path):

            shutil.copy2(label_path, dst_label)
            copied_labels += 1

        else:
            missing_labels += 1

    print(f"Copied images: {copied_images}")
    print(f"Copied labels: {copied_labels}")
    print(f"Missing labels: {missing_labels}")

# =========================================================
# DONE
# =========================================================

print("\n========================================")
print("Dataset split completed successfully!")
print("========================================")