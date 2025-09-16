import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_work_w_sep = os.path.abspath(working_directory) if os.path.abspath(working_directory).endswith(os.sep) else os.path.abspath(working_directory) + os.sep
    path = os.path.join(abs_work_w_sep, file_path)
    print(path)
    # Error handling
    if not path.startswith(abs_work_w_sep) and path != os.path.abspath(working_directory):
       return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(path):
        return f'Error: File not found or is not a reuglar file: "{file_path}"'
    
    # Read file and cut off at MAX_CHARS w/ truncate message if necessary. 
    try:
        with open(path, "r") as f:
            file_content_str = f.read(MAX_CHARS)
    except Exception as e:
        return f"Error: {e}"
    if len(file_content_str) >= MAX_CHARS:
        file_content_str += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return file_content_str
