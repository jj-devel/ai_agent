import os
from subprocess import run
from sys import executable

def run_python_file(working_directory, file_path, args=[]):
    abs_work_w_sep = os.path.abspath(working_directory) if os.path.abspath(working_directory).endswith(os.sep) else os.path.abspath(working_directory) + os.sep
    path = os.path.abspath(os.path.join(abs_work_w_sep, file_path))
    # Error handling
    if not path.startswith(abs_work_w_sep):
       return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(path):
        return f'Error: File "{file_path}" not found.'
    elif not path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = [executable, path] + args
        file_output = run(cmd,cwd=abs_work_w_sep, capture_output=True, timeout=int(30), text=True)
        if not file_output:
            return "No output produced."
        elif file_output.returncode != 0:
            return f"Process exited with code {file_output.returncode}\nSTDOUT: {file_output.stdout}\nSTDERR: {file_output.stderr}"
        return f'STDOUT: {file_output.stdout}\nSTDERR: {file_output.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"
