import os
import shutil
import datetime
import re
import getpass

# Define the base path where the folders "Input", "Error", "Archive", and TopLevels are located
base_path = r"C:/Users/username/OneDrive/Documents/Python/File Organizing System"  # Replace with the actual base path

# Define folder paths
input_folder = os.path.join(base_path, "Input")
error_folder = os.path.join(base_path, "Error")
archive_folder = os.path.join(base_path, "Archive")

# Get the current Windows username
username = getpass.getuser()

# Define a regular expression pattern to match the timestamp in the filename
timestamp_pattern = r"_(\d{14})$"

# Iterate through files in the Input folder
for filename in os.listdir(input_folder):
    if os.path.isfile(os.path.join(input_folder, filename)):
        try:
            # Parse filename and extension
            name, ext = os.path.splitext(filename)
            
            # Check if the filename already contains a timestamp and remove it if found
            name_without_timestamp = re.sub(timestamp_pattern, "", name)

            # Split the name without timestamp into levels
            levels = name_without_timestamp.split('-')

            if len(levels) != 3:
                raise ValueError(f"Invalid file name format: {filename}")

            # Extract top level, sub level, and sub-sub level
            top_level, sub_level, sub_sub_level = levels

            # Construct destination path
            dest_path = os.path.join(base_path, top_level, sub_level, sub_sub_level)

            # Ensure the destination directories exist
            os.makedirs(dest_path, exist_ok=True)

            # Create new timestamp for renaming
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

            # Construct new filename with the username and new timestamp
            new_filename = f"{name_without_timestamp}_{username}_{timestamp}{ext}"
            new_filepath = os.path.join(dest_path, new_filename)

            # Copy file to destination folder with the new timestamp and username
            shutil.copy2(os.path.join(input_folder, filename), new_filepath)

            # Construct new filename for the archive with the username and new timestamp
            archive_filename = f"{name_without_timestamp}_{username}_{timestamp}{ext}"
            archive_filepath = os.path.join(archive_folder, archive_filename)

            # Move original file to Archive folder with the username and new timestamp
            shutil.move(os.path.join(input_folder, filename), archive_filepath)
            print(f"File {filename} successfully processed and archived as {archive_filename}.")

        except Exception as e:
            # Move file to Error folder in case of failure
            shutil.move(os.path.join(input_folder, filename), os.path.join(error_folder, filename))
            print(f"Failed to process {filename}: {e}")
