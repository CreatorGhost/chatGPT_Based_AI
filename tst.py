import openai

openai.api_key = "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"


def get_data_chatGPT(title):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=title,
        temperature=0.7,
        max_tokens=450,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]["text"]

t = "how to train a dragon"

data= get_data_chatGPT(t)

print(data)