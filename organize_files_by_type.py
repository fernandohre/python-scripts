import os

# create a function to get files type from a folder
def get_files_type(path):
    files = os.listdir(path)
    files_type = []
    for file in files:
        if os.path.isfile(os.path.join(path, file)) and file.split('.')[-1].lower() not in files_type:
            files_type.append(file.split('.')[-1].lower())
    return files_type

def create_folders_from_files_type(path, files_type):
    for file_type in files_type:
        if not os.path.exists(os.path.join(path, file_type)):
            os.mkdir(os.path.join(path, file_type))

# get files grouped by folder
def get_files_grouped_by_type(path, file_type):
    files_type = get_files_type(path)
    files_grouped_by_type = []
    for file_type in files_type:
        files_of_type = []
        for file in os.listdir(path):
            if file.split('.')[-1].lower() == file_type:
                files_of_type.append(file)

        files_grouped_by_type.append({
            'type': file_type,
            'files': files_of_type
        })
    return files_grouped_by_type


def move_files_to_corresponding_folder(files_grouped_by_type):
    for file_group in files_grouped_by_type:
        for file in file_group['files']:
            os.replace(os.path.join(path_to_organize, file), os.path.join(path_to_organize, file_group['type'], file))

path_to_organize = input('What path do you want to organize? (paste here): ')
print('You entered: ' + path_to_organize)

# get files type from a folder
files_type = get_files_type(path_to_organize)
print('You have the following files type in your folder: ' + ','.join(files_type))

create_folders_from_files_type(path_to_organize, files_type)
files_grouped_by_type = get_files_grouped_by_type(path_to_organize, files_type)
os.chdir(path_to_organize)
print('Moving files to folders...')
move_files_to_corresponding_folder(files_grouped_by_type)
