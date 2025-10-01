import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
# Function Schemas
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_files_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file

# Check for required arguments
if len(sys.argv) < 1:
    print("ERROR: Missing prompt conents, please add a <'string'> argument after the program call. ")
    sys.exit(0)
prompt = str(sys.argv[1])

# Constant prompt for the AI to follow at all times
SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# Functions that the AI can use
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content, 
        schema_write_file, 
        schema_run_python_file, 
    ]
)

# Get api key from env and load into client
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# User input
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]

# AI model creation
output = client.models.generate_content(
model="gemini-2.0-flash-001", 
contents=messages, 
config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT), 
)

# Extra information for the {--verbose} argument
verbose_arg = f"""User prompt: {prompt}
Prompt tokens: {output.usage_metadata.prompt_token_count}
Response tokens: {output.usage_metadata.candidates_token_count}
"""

def main():
    # Verbose
    if "--verbose" in str(sys.argv):
        print(verbose_arg)
    # Question
    if output.function_calls == None:
        print(f"Output: {output.text}")
    else: 
        print(f"Calling function: {output.function_calls[0].name}({output.function_calls[0].args})")

if __name__ == "__main__":
    main()
