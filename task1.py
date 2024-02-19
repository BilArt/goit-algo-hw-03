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

def main():
    parser = argparse.ArgumentParser(description="Copy files recursively and sort them by extension")
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument("destination_dir", nargs="?", type=str, default="dist", help="Path to the destination directory (default: dist)")
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    copy_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
