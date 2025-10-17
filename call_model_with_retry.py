# python
from google import genai
from google.genai import types
import time
from google.genai.errors import ServerError

def call_model_with_retry(client, messages, available_functions, system_prompt, retries=5, delay=1.0):
    attempt = 0
    while True:
        try:
            return client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt,
                ),
            )
        except ServerError as e:
            if getattr(e, "status_code", None) == 503 and attempt < retries:
                attempt += 1
                time.sleep(delay)
                continue
            # print graceful message and return a fake no-function-call response
            print("The model is overloaded. Please try again shortly.")
            # Return an object with no function_calls so your main prints output.text
            # If returning None is easier, handle that in main.
            return None
