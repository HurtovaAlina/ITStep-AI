import dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages,
)

# завантадити дані з .env
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
    Ти -- ввічливий чатбот
    Твоя задача підтримувати спілкування з користувач

    ###ІНСТРУКЦІЇ###
    1. Відповіді мають дути короткими(до 2 речень)
    """),

    # всі наступні елементи в списку -- повідомлення від користувач та відповіді llm
    HumanMessage("Привіт"),
    AIMessage("Привіт, як справи?"),
    HumanMessage("Порекомендуй цікавий фільм"),
]

# використання моделі
# моделі треба передати всю історію спілкування
# response = llm.invoke(messages)
#
# print(type(response))
# print(response)


# чатбот

# створенні списку для історії повідомлень(ише інструкції)
messages = [
    SystemMessage("""
    Ти -- ввічливий чатбот
    Твоя задача підтримувати спілкування з користувач

    ###ІНСТРУКЦІЇ###
    1. Відповіді мають дути короткими(до 2 речень)
    """)
]

# # цикл для спілкування
# while True:
#     # отримати повідомлення від користувача
#     user_text = input("Ви: ")
#
#     # перевірка для кінця спілкування
#     if user_text == "":
#         break
#
#     # створити HumanMessage
#     human_message = HumanMessage(content=user_text)
#
#     # додати повідемлення в історії
#     messages.append(human_message)
#
#     # отримати відповідь моделі
#     response = llm.invoke(messages)
#
#     # вивести на екран відповідь
#     print(f"AI: {response.content[0]['text']}")
#
#     # добавити response в історію спілкування
#     messages.append(response)
#
#
#     # # вивести історію спілкування
#     # print()
#     # print("----------------------------------")
#     # print("HISTORY")
#     # for message in messages:
#     #     print(message)
#     # print("----------------------------------")
#     # print()


# очищення історії від зайвих повідомлень

# # створення трімера повідомлень
# trimmer = trim_messages(
#     strategy='last',  # залишати останні повідомлення
#
#     token_counter=len,  # рахуємо кількість повідомлень
#     max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)
#
#     start_on='human',  # історія завжди починатиметься з HumanMessage
#     end_on='human',  # історія завжди закінчуватиметься з HumanMessage
#     include_system=True  # SystemMessage не чіпати
# )
#
# # цикл для спілкування
# while True:
#     # отримати повідомлення від користувача
#     user_text = input("Ви: ")
#
#     # перевірка для кінця спілкування
#     if user_text == "":
#         break
#
#     # створити HumanMessage
#     human_message = HumanMessage(content=user_text)
#
#     # додати повідемлення в історії
#     messages.append(human_message)
#
#     # очищення історії
#     messages = trimmer.invoke(messages)
#
#     # отримати відповідь моделі
#     response = llm.invoke(messages)
#
#     # вивести на екран відповідь
#     print(f"AI: {response.content[0]['text']}")
#
#     # добавити response в історію спілкування
#     messages.append(response)
#
#
#     # вивести історію спілкування
#     print()
#     print("----------------------------------")
#     print("HISTORY")
#     for message in messages:
#         print(message)
#     print("----------------------------------")
#     print()


# трімер можна об'єднати з моддю в ланцюг

# створення трімера повідомлень
trimmer = trim_messages(
    strategy='last',  # залишати останні повідомлення

    token_counter=len,  # рахуємо кількість повідомлень
    max_tokens=5,  # залишати максимум 5 повідомлення(System, AI, Human)

    start_on='human',  # історія завжди починатиметься з HumanMessage
    end_on='human',  # історія завжди закінчуватиметься з HumanMessage
    include_system=True  # SystemMessage не чіпати
)

# ланцюг
chain = trimmer | llm

# цикл для спілкування
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
    response = chain.invoke(messages)

    # вивести на екран відповідь
    print(f"AI: {response.content[0]['text']}")

    # добавити response в історію спілкування
    messages.append(response)

    # вивести історію спілкування
    print()
    print("----------------------------------")
    print("HISTORY")
    for message in messages:
        print(message)
    print("----------------------------------")
    print()