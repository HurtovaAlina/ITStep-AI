# створення агентів
# агент -- чат-бот(llm) + інструменти

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
    serper_api_key=serper_key
)


# інструменти

@tool
def product(a: float, b: float) -> float:
    """
    Множить два дійсних числа між собою

    :param a: float -- перше число
    :param b: float -- друге число
    :return: float -- добуток чисел
    """

    print("hi from product tool")
    return a * b


@tool
def get_weather(city: str, hour: int) -> str:
    """
    Повіретає інформацію про погоду в місті

    :param city: str -- назва міста
    :param hour: int -- година дня окотрій шукати інвормацію про погоду(0-24)
    :return: прогноз погоди
    """
    print("hi from get_weather tool")
    return f"Погода в {city} о {hour}-ій годині буде сонячна але з хмарами"


@tool
def google_search(query: str):
    """
    Зукає інформацію в інтернеті

    :param query: str -- запит в пошуковик
    :return: результат пошуку
    """

    print("hi from google_search tool")
    result = serper_search.results(query)
    print(result)

    return result


# створення агента
agent = create_agent(
    model=llm,  # нейромережа агента
    tools=[product, get_weather, google_search],  # список інструментів
)

# написати системний промпт
# разом з ним створюємо історією повідослень

messages = [
    SystemMessage("""
    Ти -- ввічлиіий чат бот

    у тебе є доступ до інструментів
    * product
    * get_weather

    ###ІНСТРУКЦІЯ###
    1. якщо користувач не вказує назву міста або годину при запиті про погоду, то ти повенен уточнити пропущену інформаці
    """)
]

# цикл зі спідкуванням
while True:
    # Запит від користувача
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