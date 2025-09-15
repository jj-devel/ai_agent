import os

def get_file_content(working_directory, file_path):
    abs_work_w_sep = os.path.abspath(working_directory) if os.path.abspath(working_directory).endswith(os.sep) else os.path.abspath(working_directory) + os.sep

    if not file_path.startswith(abs_work_w_sep) and file_path != os.path.abspath(working_directory):
       return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(file_path):
        return f'Error: File not found or is not a reuglar file: "{file_path}"'
    
    pass