import glob
import os

# Define the directories to search
directories = ["ids590_specific/exercises_590", "ids720_specific/exercises"]

# Find and rename files in each directory
for directory in directories:
    # Find all .ipynb files starting with "Exercise_"
    pattern = os.path.join(directory, "Exercise_*.ipynb")
    files = glob.glob(pattern)

    for file_path in files:
        # Get the directory and filename separately
        dir_name = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)

        # Create new filename with lowercase 'e'
        new_file_name = file_name.replace("Exercise_", "exercise_", 1)
        new_file_path = os.path.join(dir_name, new_file_name)

        # Rename the file
        print(f"Renaming: {file_path} -> {new_file_path}")
        os.rename(file_path, new_file_path)

print("Done!")
