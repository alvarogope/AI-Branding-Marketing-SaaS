import anthropic
from dotenv import load_dotenv
import argparse
import re

MAX_INPUT_LENGTH = 20

def main():

    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User Input: {user_input}")
    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
          f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is '{user_input}'"
        )

def validate_length(user_input) -> bool:
    return len(user_input) <= MAX_INPUT_LENGTH

def generate_keywords(user_input):
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=12,
        messages=[
            {
                "role": "user",
                "content": f"Generate related branding keywords for {user_input}",
            }
        ],
    )

    keywords_text: str = message.content[0].text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)

    print(f"Keywords: {keywords_array}")
    return keywords_array

def generate_branding_snippet(user_input):
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": f"Generate related branding snippet for {user_input}",
            }
        ],
    )

    branding_text = message.content[0].text.strip()
    print(f"Snippet: {branding_text}")
    return branding_text

if __name__ == "__main__":
    main()