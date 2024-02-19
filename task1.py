import os
import shutil
import argparse

def copy_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            destination_subdir = os.path.join(destination_dir, extension)
            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)
            try:
                shutil.copy(file_path, destination_subdir)
                print(f"Successfully copied {file} to {destination_subdir}")
            except Exception as e:
                print(f"Error copying {file}: {e}")
