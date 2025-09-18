import os

def write_file(working_directory, file_path, content):
    abs_work_w_sep = os.path.abspath(working_directory) if os.path.abspath(working_directory).endswith(os.sep) else os.path.abspath(working_directory) + os.sep
    path = os.path.abspath(os.path.join(abs_work_w_sep, file_path))
    dir_name = os.path.dirname(path)
    # Error handling
    if not path.startswith(abs_work_w_sep) and path != os.path.abspath(working_directory):
       return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif dir_name:
        os.makedirs(dir_name, exist_ok=True)

    try:
        with open(path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
