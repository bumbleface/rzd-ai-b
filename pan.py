import pandas as pd
from gpt4all import GPT4All
import gtts
from gtts import gTTS
from playsound import playsound
model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", allow_download=False)


xl = pd.ExcelFile('file1.xlsx')
df = xl.parse('Sheet1')

questions_merged = df['questions_merged']
answers_merged = df['answers_merged']


with model.chat_session():
    response1 = model.generate(prompt=f"pick one question. don't write anything else, just pick a question: {questions_merged}")
    print(model.current_chat_session)
    print("Введите ответ: ")
    answer = str(input())
    response2 = model.generate(prompt=f"{answer} - check if this answer is correct or not by looking at this table: {questions_merged} {answers_merged} if it's not then")
    print(model.current_chat_session)




