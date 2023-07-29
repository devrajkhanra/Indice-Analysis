# modules/file_checker.py

import os
import glob

def find_files_on_desktop(folder_name, file_pattern):
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    target_folder_path = os.path.join(desktop_path, folder_name)
    file_pattern = os.path.join(target_folder_path, file_pattern)

    # Check if the target folder exists
    if not os.path.exists(target_folder_path):
        print(f"The folder '{folder_name}' does not exist on the desktop.")
        return []

    # Find files that match the given pattern
    matched_files = glob.glob(file_pattern)


    return matched_files
