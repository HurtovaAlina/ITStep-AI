# Завдання 1
# Підключіть модель LLM за допомогою свого API key.
# Попросіть модель згенерувати:


# Підберіть параметри креативності та довжини

import dotenv
import os

import langchain
from langchain_google_genai import GoogleGenerativeAI

# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(
    model="gemini-3.5-flash-lite",   # назва моделі
    api_key=api_key,    # ключ до сервера з моделлю
    # temperature =0.9, # температура впливає на креативність, чим більша креативність, тим більше температура
    # top_p=0.8,
    # top_k=10

)

# ● відповідь на питання у вигляді одного
# слова(наприклад яка столиця Франції?)
# response =llm.invoke("яка столиця Ліхтенштейну, одним словом")
# print(response)

# # ● код python
# response =llm.invoke("напиши функцію на пайтон для розрахунку факторіала, оформи як окрему функцію, тільки пайтон")
# print(response)

# # ● коротку історію
# response =llm.invoke("напиши коротку історію про програміста, який не може віддебажити код. Близько 6 речень")
# print(response)

# Завдання 2
# Прочитайте файл data\lesson9\rules.txt з правилами
# користування атракціону. Напишіть програму яка отримує
# від користувачі питання та дає відповідь на нього виходячи
# з текстового файлу.
# Для цього об’єднайте правила користування з питанням
# користувача.
# Користувач задає питання поки не введе порожній рядок.
# Змініть файл rules.txt, щоб переконатись що модель
# дійсно його читає.


with open("data/lesson9/rules.txt", "r", encoding ="utf-8") as file:
    text = file.read()
    # print(text)

# while True:
#     question = input("Введіть запитання щодо користування атракціоном ")
#
#     if question == "":
#         break
#
#     response =llm.invoke(f"""прочитай правила користування атракціоном, збережені в {text}
#     прочитай питання  користувача {question}, і знайдаи відповідь стосовно правил, з посиланням на пункт правил, якщо
#     немає в правилах, не вигадуй, а напиши, що правилами не передбачена така ситуація""")
#     print(response)

# Завдання 3
# Створіть найпростіший чат бот. Напишіть моделі якого
# персонажа вона повинна вдавати(відомий актор, персонаж
# кіно\книги, тощо).
# Реалізуйте двома способами:
# 1. Модель отримує інструкцію в якому стилі відповідати
# та нове повідомлення.
# 2. Модель отримує інструкцію та історію попередніх
# повідомлень як від користувача, так і її власні відповіді у
# форматі
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:


questions = []
responses = []

instructions = f"""прочитай правила користування атракціоном, збережені в {text} 
    прочитай питання  користувача, 
    і знайдаи відповідь стосовно правил, з посиланням на пункт правил, якщо 
    немає в правилах, не вигадуй, а напиши, що правилами не передбачена така ситуація. 
"""


while True:
    question = input("Введіть запитання щодо користування атракціоном ")
    if question == "":
        break

    history = ""

    for old_question, old_response in zip(questions, responses):
        history += f"\nUser: {old_question}"
        history += f"\nModel: {old_response}"

    chat = f"""
    {instructions}
        
    Історія спілкування:
    {history}
    User: {question}
    Model: 
    """

    response =llm.invoke(chat)

    print(f"Відповідь: {response}")

    questions.append(question)
    responses.append(response)
#показати історію
print("==== HISTORY =====")

history = ""

for question, response in zip(questions, responses):
    history += f"\nUser: {question}"
    history += f"\nModel: {response}"

print(history)