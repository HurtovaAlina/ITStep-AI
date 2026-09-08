# Завдання 1
# Напишіть чат бота, з інструментом по рекомендації
# ресторанів.
# Для цього скористайтесь
# GoogleSerperAPIWrapper(type="places")
# Інструмент повинен отримувати запит для пошуку та
# повертати таку інформацію про ресторани:
#  назва
#  посилання на сайт(якщо є)
#  рейтинг
# Більш детально дивись документацію

import dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    BaseMessage,
    trim_messages,
)

# завантадити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

serper_search = GoogleSerperAPIWrapper(
    serper_api_key=serper_key,
    type="places",
)


# інструменти

@tool
def google_search(query: str) -> list[dict]:
    """
    Шукає ресторани за запитом.

    :param query: пошуковий запит, наприклад: "італійські ресторани в Ужгороді"
    :return: список ресторанів з назвою, сайтом та рейтингом
    """

    result = serper_search.results(query)

    restaurants = []

    for place in result.get("places", []):
        restaurants.append({
            "name": place.get("title"),
            "link": place.get("website"),
            "rating": place.get("rating"),
            "address": place.get("address")
        })

    return restaurants


# створення агента
agent = create_agent(
    model=llm,  # нейромережа агента
    tools=[google_search],  # список інструментів
)

# написати системний промпт
# разом з ним створюємо історією повідослень

messages = [
    SystemMessage("""
    Ти -- ввічлиіий чат бот

    у тебе є доступ до інструментів
    *  google_search
    

    ###ІНСТРУКЦІЯ###
    1. Користувач надає запит для пошуку ресторанів (напариклад, італійські ресторани в Ужгороді), ти повинен 
    використовуючи інтсрумент, знайти ресторан, надати користувачу наступну інформацію: назву, веб сайт,  рейтинг
    та адресу.
    Якщо немає веб сайту, або рейтингу - напиши, що інформації не знайдено. 
    Інформацію надавай в порядку зменшення рейтингу (спочатку ресторани з найбільшим рейтингом)
    """)
]

# цикл зі спідкуванням
while True:
    # Запит від користувача
    print("Введіть ресторан і місце, де би Ви хотіли його відвідати")
    user_query = input("Ви: ")

    # умова закінчення
    if user_query == "":
        break

    # зробити human message
    user_message = HumanMessage(user_query)

    # добавляємо повідомлення в історію
    messages.append(user_message)

    # отримати відповіть від агента
    # агент сам дадає повідемлення в історію і повертає її

    # агент треба передавати словник зі ключем "messages"
    data = {
        "messages": messages
    }

    data = agent.invoke(data)
    # агент так само повертає словник

    # дістаємо нову історію повідомлень
    messages = data["messages"]

    # відповідь моделі -- останнє повідомлення в історії
    response = messages[-1]

    # вивести відповідь на екран
    print(response.text)

    # виведення історії
    print()
    print("----------ІСТОРІЯ-----------")

    for message in messages:
        print(repr(message))  # вивести разом з назсою класу

    print("-----------------------------")
    print()