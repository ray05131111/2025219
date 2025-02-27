from openai import OpenAI
import os
# client = OpenAI(api_key=os.getenv('open_apikey'))
client = OpenAI(api_key='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')


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是中國人"},
        {
            "role": "user",
            "content": "講一句話"
        }
    ]
)

print(completion.choices[0].message.content)