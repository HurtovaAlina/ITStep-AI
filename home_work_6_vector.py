# Завдання 1
# Добавте в створену базу даних файл
# data/lesson_rag/huge_file.txt про умови користування гуглом
# Оскільки файл надто великий, то його треба добавляти
# частинами. Для цього:
#  прочитайте вміст файлу
#  розділіть його на окремі блоки(між блоками два
# порожніх рядка, дивись файл)
#  отримайте перший рядок кожного блоку – це його
# назва
#  створіть документи для кожного блоку. В метаданих:
# o назва файлу
# o назва блоку
#  створіть ID та добавте все в існуючу базу даних
#  добавте ID у json файл
#  перевірте агента

import dotenv
import os
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.agents import create_agent
from langchain_core.tools import tool
from pinecone import ServerlessSpec
from pinecone import Pinecone
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    BaseMessage,
    trim_messages,
)
# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key,
)

pc = Pinecone(api_key=pinecone_api_key)

# створення бази даних

index_name = "home-work6"  # назва бази даних

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
    Пошук документів у вектоній базі даних, яка містить інформацію про ЗАГАЛЬНІ ПОЛОЖЕННЯ ТА УМОВИ GOOGLE

    База даних містить інформацію про правила користування сервісом GOOGLE
    :param query: str -- запит від користувача
    :return:  схожі документи
    """

    results = vector_store.similarity_search(
        query,  # текст для пошуку схожих документів
        k=5,  # кількість документів яку шукаємо
    )

    return results

# створення агента
agent = create_agent(
    model=llm,  # нейромережа агента
    tools=[document_search],  # список інструментів
)

# написати системний промпт
# разом з ним створюємо історією повідослень

messages = [
    SystemMessage("""
    Ти -- ввічлиіий чат бот

    ###ІНСТРУКЦІЯ###
    1. якщо користувач питає щось про правила користування сервісом GOOGLE, то використовуюй document_search 
    2. надай інформацію, знайдену в документі 
    3. якщо немає релевантної інформації нічого не вигадуй, відповідай, що в документі не знайдено. 
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
