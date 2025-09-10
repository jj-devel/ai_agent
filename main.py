import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

if len(sys.argv) < 1:
    print("ERROR: Missing prompt conents, please add a <'string'> argument after the program call. ")
    sys.exit(0)
prompt = str(sys.argv[1])

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]

output = client.models.generate_content(
model="gemini-2.0-flash-001", 
contents=messages, 
)

verbose_arg = f"""User prompt: {prompt}
Prompt tokens: {output.usage_metadata.prompt_token_count}
Response tokens: {output.usage_metadata.candidates_token_count}
"""

def main():
    # Verbose
    if "--verbose" in str(sys.argv):
        print(verbose_arg)
    # Question
    print(f"Output: {output.text}")

if __name__ == "__main__":
    main()
