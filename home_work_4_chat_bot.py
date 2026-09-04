# Завдання 1
# Напишіть чат модель яка підсумовує всю розмову в
# декілька речень. Вкажіть щоб модель зберігала якомога
# більше деталей.
# Використайте цю модель для простого чат бота який
# замість trim_massages використовує модель з підсумуванням.
# Підсумовуйте повідомлення, коли їх більше 4.
# Старі повідомлення треба видалити
# НЕ ВИДАЛЯТИ SystemMessage та не використовувати
# його для підсумування

import dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)

# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

# # історія повідомлень
messages = [
    # список усіх повідомлень в чаті
    # на початку завжди йде SystemMessage -- з інструкціями для чатботу
    SystemMessage("""
    Ти --  чатбот
    Твоя задача підтримувати дружнє і цікаве спілкування з користувачем 

    ###ІНСТРУКЦІЇ###
    1. Відповіді мають бути короткими(1-2 речення)
    """)
]
summary_chat_bot = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

# # підсумування
summary = """
Ти -- уважний чатбот.
Твоя задача підсумувати всю розмову в декілька речень. Зберігай якомога більше деталей.

### ІНСТРУКЦІЇ ###
1. Підсумок має бути коротким (1-2 речення) і містити основний контекст розмови та бути зрозумілим.

### ВХІДНІ ДАНІ ###
Повідомлення: {messages}
"""

# чатбот
# # цикл для спілкування
while True:
    # отримати повідомлення від користувача
    user_text = input("Ви: ")

    # перевірка для кінця спілкування
    if user_text == "":
        break

    # створити HumanMessage
    human_message = HumanMessage(content=user_text)

    # додати повідемлення в історії
    messages.append(human_message)

    # отримати відповідь моделі
    response = llm.invoke(messages)

    # вивести на екран відповідь
    print(f"AI: {response.content[0]['text']}")

    # добавити response в історію спілкування
    messages.append(response)

    # кількість повідомлень без SystemMessage
    if len(messages) - 1 > 4:
        # вивести історію спілкування
        print()
        print("----------------------------------")
        print("HISTORY")
        for message in messages:
            print(message.content)
        print("----------------------------------")
        print()

        # повідомлення без SystemMessage
        main_content = messages[1:]

        # промпт для моделі підсумування
        summary_prompt = summary.format(
            messages=main_content
        )

        # підсумок розмови
        response_summary = summary_chat_bot.invoke(summary_prompt)

        print("SUMMARY")
        print(response_summary.content)

        # видалити старі повідомлення
        # залишити SystemMessage + summary
        messages = [
            messages[0],
            AIMessage(content=f"Підсумок попередньої розмови: {response_summary.content}")
        ]


