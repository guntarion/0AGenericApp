import os

def sanitize_filename(filename):
    # Unsafe characters for Windows and Mac
    unsafe_characters = '<>:"/\\|?*:'
    for char in unsafe_characters:
        filename = filename.replace(char, '_')
    return filename

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        sanitized_filename = sanitize_filename(filename)
        if filename != sanitized_filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, sanitized_filename))
            print(f"Renamed file: {filename} to {sanitized_filename}")

# Specify the directory
directory = r"C:\Users\LEGION 5 PRO\Downloads\DALLE Images"
rename_files_in_directory(directory)