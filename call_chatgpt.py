from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key=api_key
)

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant to provide recipes from all around the world."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Controls the randomness of responses
            max_tokens=500,  # Adjust for response length
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == '__main__':
    user_prompt = "What is the capital of France?"
    response = chat_with_gpt(user_prompt)
    print(response)
