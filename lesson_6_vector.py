# створення агентів
# агент -- чат-бот(llm) + інструменти


import dotenv
import os
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from pinecone import ServerlessSpec
from pinecone import Pinecone
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
# serper_key = os.getenv("SERPER_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")


# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

# serper_search = GoogleSerperAPIWrapper(
#     serper_api_key=serper_key
# )

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key,
)

pc = Pinecone(api_key=pinecone_api_key)

# створення бази даних

index_name = "itset-docs"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=3072,    # кількість чисел у векторі
        metric="cosine",   # формула для пошуку схожих текстів
        spec=ServerlessSpec(
            cloud="aws",        # хмарна платформа(амазон)
            region="us-east-1"  # регіон
        ),
    )

index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,          # база даних
    embedding=embedding   # модель для кодування
)


# інструменти
@tool
def document_search(query: str):
    """
    Пошук документів у вектоній базі даних

    База даних містить інформацію про суп та нашу компанію
    :param query: str -- запит від користувача
    :return:  схожі документи
    """

    results = vector_store.similarity_search(
        query,  # текст для пошуку схожих документів
        k=2,  # кількість документів яку шукаємо
    )

    return results


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


# @tool
# def google_search(query: str):
#     """
#     Зукає інформацію в інтернеті
#
#     :param query: str -- запит в пошуковик
#     :return: результат пошуку
#     """
#
#     print("hi from google_search tool")
#     result = serper_search.results(query)
#     print(result)
#
#     return result


@tool
def save_json(data: dict):
    """
    берігає дані в json файл
    :param data: dict -- дані
    :return:
    """

    with open("file.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

# створення агента
agent = create_agent(
    model=llm,  # нейромережа агента
    tools=[product, get_weather, document_search, save_json],  # список інструментів
)

# написати системний промпт
# разом з ним створюємо історією повідослень

messages = [
    SystemMessage("""
    Ти -- ввічлиіий чат бот

    ###ІНСТРУКЦІЯ###
    1. якщо користувач не вказує назву міста або годину при запиті про погоду, то ти повенен уточнити пропущену інформаці
    2. якщо користувач питає щосб про суп або наша компанія то використовуюй document_search
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