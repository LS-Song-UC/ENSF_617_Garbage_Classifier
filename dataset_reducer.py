import os
import random

def reduce_png_count(target_folders, target_count):
    for folder in target_folders:
        if not os.path.exists(folder):
            print(f"Folder not found: {folder}")
            continue

        # Filter for PNG files only
        files = [f for f in os.listdir(folder) if f.lower().endswith('.png')]
        current_count = len(files)

        if current_count <= target_count:
            print(f"'{folder}' already has {current_count} PNGs. No action needed.")
            continue

        # Calculate how many to delete
        to_delete_count = current_count - target_count
        to_delete_files = random.sample(files, to_delete_count)

        print(f"Reducing '{folder}' from {current_count} to {target_count}...")

        for file_name in to_delete_files:
            file_path = os.path.join(folder, file_name)
            os.remove(file_path)

        print(f"Successfully removed {to_delete_count} files from '{folder}'.")

# Concrete folder examples
my_folders = [
    './garbage_data/CVPR_2024_dataset_Train/Black',
    './garbage_data/CVPR_2024_dataset_Train/Blue',
    './garbage_data/CVPR_2024_dataset_Train/Green',
    './garbage_data/CVPR_2024_dataset_Train/TTR',
    './garbage_data/CVPR_2024_dataset_Test/Black',
    './garbage_data/CVPR_2024_dataset_Test/Blue',
    './garbage_data/CVPR_2024_dataset_Test/Green',
    './garbage_data/CVPR_2024_dataset_Test/TTR',
    './garbage_data/CVPR_2024_dataset_Val/Black',
    './garbage_data/CVPR_2024_dataset_Val/Blue',
    './garbage_data/CVPR_2024_dataset_Val/Green',
    './garbage_data/CVPR_2024_dataset_Val/TTR',
]

# Run the reduction
reduce_png_count(my_folders, target_count=50)