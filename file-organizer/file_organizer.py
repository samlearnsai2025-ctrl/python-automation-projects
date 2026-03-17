import os
import shutil

directory_path = input("Enter the directory path to organize: ")

categories = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.mp4': 'Videos',
    '.py': "Code"
}

move_log = []

for file in os.listdir(directory_path):
    # skip if it's a folder, not a file
    if os.path.isfile(os.path.join(directory_path, file)):

        # get the extension
        name, extension = os.path.splitext(file)

        # look up with categories it belongs to
        folder_name = categories.get(extension, "Others")

        # build full path of the file (where it is currently is)
        source = os.path.join(directory_path, file)

        # build destination folder path
        destination_folder = os.path.join(directory_path, folder_name)

        # create the folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        # each time you move a file, record it
        move_log.append((source, destination_folder))

        # move the file
        shutil.move(source, destination_folder)

        print(f"Moved: {file} to {destination_folder}")

print("Organization complete!")

undo = input("Do you want to undo the organization? (yes/no): ")

folder_for_delete = set(destination_folder for _, destination_folder in move_log)

if undo.lower() == 'yes':
    for source, destination_folder in move_log:
        shutil.move(os.path.join(destination_folder, os.path.basename(source)), source)

    for folder in folder_for_delete:
        try:
            # remove the folder if it's empty
            os.rmdir(folder)
        except OSError:
            print(f"Could not remove folder (not empty): {folder}")
    
    print("Undo complete!")


        