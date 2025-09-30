import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    path = os.path.abspath(os.path.join(working_directory, directory))
    abs_work_w_sep = os.path.abspath(working_directory) if os.path.abspath(working_directory).endswith(os.sep) else os.path.abspath(working_directory) + os.sep

    if not path.startswith(abs_work_w_sep) and path != os.path.abspath(working_directory):
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    path_list = os.listdir(path)
    files_info = []
    for item in path_list:
        files_info.append(f"- {item}: file_size={os.path.getsize(os.path.join(path, item))} bytes, is_dir={os.path.isdir(os.path.join(path, item))}")
    return "\n".join(files_info)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
