def get_files_info(working_directory, directory="."):
    if os.path.abspath(directory) not in working_directory:
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif  not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    path = os.path.join(working_directory, directory)
    path_list = os.listdir(path)
    files_info = []
    for item in path_list:
        files_info.append(f"- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}")
    return "\n".join(files_info)