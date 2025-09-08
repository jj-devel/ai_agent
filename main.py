import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

first_question = client.models.generate_content(model="gemini-2.0-flash-001", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

def main():
    # Question
    print(first_question.text)
    # Token count
    print(f"Prompt tokens: {first_question.usage_metadata.prompt_token_count}\nResponse tokens: {first_question.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
