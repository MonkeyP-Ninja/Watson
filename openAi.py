import os
import openai

openai.organization = "org-ExNEkFygQ66RvSjsITNnB13k"
openai.api_key = "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"


def wattson(text):
  start_sequence = "\nAI:"
  restart_sequence = "\nHuman: "

  response = openai.Completion.create(
    engine="davinci",
    prompt=text,
    temperature=0.19,
    max_tokens=80,
    top_p=1,
    frequency_penalty=1.17,
    presence_penalty=0.16,

  )


  content = response.choices[0].text


while True:

  wattson(text=input('type :'))
