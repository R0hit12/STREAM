import time
from openai import OpenAI

# Define the function to send partial input messages and receive partial completions
def stream_chat(client, messages, model="openai/gpt-3.5-turbo"):
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        stream=True
    )
    animal_number = 1
    for chunk in response:
        if chunk.choices:
            for choice in chunk.choices:
                completion = choice.delta.content.strip()
                # Check if completion is not empty and doesn't start with a number
                if completion and not completion[0].isdigit():
                    print(f"{animal_number}. {completion}")
                    animal_number += 1
        else:
            time.sleep(0.1)  # Add a small delay to avoid excessive API calls

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# Define the messages
messages = [
    {"role": "user", "content": "Name 10 animals"},
]

# Call the function to stream the chat
stream_chat(client, messages)
