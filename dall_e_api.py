import openai


def call_dall_e(input_text, api_key):
    openai.api_key = api_key
    return openai.Image.create(
        prompt=input_text,
        n=5,
        size="1024x1024"
    )
