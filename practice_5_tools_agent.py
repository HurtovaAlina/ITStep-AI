# Завдання 1
# Напишіть функцію яка перевіряє складність паролю:
#  кількість символів(>8)
#  наявність хоча б однієї літери\цифри\спеціального
# символу
#  наявність літер в різних регістрах
# Функція повертає тест з описом паролю(що добре, а що
# погано)
# На основі цієї функції створіть агента.

import dotenv
import os
import re

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    BaseMessage,
    trim_messages,
)
from openai import BaseModel
from pydantic import Field

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

# @tool
# def password_complexity(password: str) -> str:
#     """
#     Перевіряє складність паролю
#     #  кількість символів(>8)
#     #  наявність хоча б однієї літери\цифри\спеціального символу
#     #  наявність літер в різних регістрах
#
#     :param : password: str -- пароль
#     :return: Функція повертає тест з описом паролю(що добре, а що погано)
#     """
#     complexity = ""
#
#     if len(password) <= 8:
#         length = "Length of password lees or equal 8 "
#     else:
#         length = "Length of password meets the condition "
#
#
#     if re.search(r"[a-z]", password):  # # є маленька літера
#         lowercase_letter = "At least one lowercase letter is present "
#     else:
#         lowercase_letter = "At least one lowercase letter is NOT present "
#
#     if re.search(r"[A-Z]", password): # є велика літера
#         uppercase_letter = "At least one uppercase letter is present "
#     else:
#         uppercase_letter = "At least one uppercase letter is NOT present "
#
#     if re.search(r"\d", password): # є цифра
#         digit = "At least one digit is present "
#     else:
#         digit = "At least one digit is NOT present "
#
#     if re.search(r"[^A-Za-z0-9]", password): # є спецсимвол
#         symbol = "At least one symbol is present "
#     else:
#         symbol = "At least one symbol is NOT present "
#
#     complexity = length + lowercase_letter + uppercase_letter + digit + symbol
#     return complexity
#
# # створення агента
# agent = create_agent(
#     model=llm,  # нейромережа агента
#     tools=[password_complexity],  # список інструментів
# )
#
# # написати системний промпт
# # разом з ним створюємо історією повідослень
#
# messages = [
#     SystemMessage("""
#     Ти -- ввічлиіий чат бот
#
#     у тебе є доступ до інструментів
#     * password_complexity
#
#     ###ІНСТРУКЦІЯ###
#     1. користувач надає пароль, тобі треба зробити висновок про його складність
#     """)
# ]
#
# # цикл зі спідкуванням
# while True:
#     # Запит від користувача
#     user_query = input("Ви: ")
#
#     # умова закінчення
#     if user_query == "":
#         break
#
#     # зробити human message
#     user_message = HumanMessage(user_query)
#
#     # добавляємо повідомлення в історію
#     messages.append(user_message)
#
#     # отримати відповіть від агента
#     # агент сам дадає повідемлення в історію і повертає її
#
#     # агент треба передавати словник зі ключем "messages"
#     data = {
#         "messages": messages
#     }
#
#     data = agent.invoke(data)
#     # агент так само повертає словник
#
#     # дістаємо нову історію повідомлень
#     messages = data["messages"]
#
#     # відповідь моделі -- останнє повідомлення в історії
#     response = messages[-1]
#
#     # вивести відповідь на екран
#     print(response.text)
#
#     # виведення історії
#     print()
#     print("----------ІСТОРІЯ-----------")
#
#     for message in messages:
#         print(repr(message))  # вивести разом з назсою класу
#
#     print("-----------------------------")
#     print()


# Завдання 2
# Напишіть модель показує останні новини про певну
# людину. Якщо користувач вводить не ім’я людини, то вивести
# повідомлення «немає відповідної інформації»
# Скористайтесь DuckDuckGoSearchRun

# @tool
# def search() -> str:
#     """
#     Показує останні новини про певну людину, якщо користувач вводить не ім’я людини, то вивести
#     повідомлення «немає відповідної інформації»
#     :param : name: str -- імʼя людини
#     :return: Функція повертає останні новини про певну людину
#     """
#     search = DuckDuckGoSearchRun()
#     return search
#
#
# # створення агента
# agent = create_agent(
#     model=llm,  # нейромережа агента
#     tools=[search],  # список інструментів
# )
#
# # написати системний промпт
# # разом з ним створюємо історією повідослень
#
# messages = [
#     SystemMessage("""
#     Ти -- ввічлиіий чат бот
#
#     у тебе є доступ до інструментів
#     * search
#
#     ###ІНСТРУКЦІЯ###
#     1. користувач надає імʼя людини, новини про яку він хоче дізнатися. Твоя задача знайти актуальну
#     інформацію про цю людину. Якщо інформація не знайдена, або користувач ввів не імʼя людини,
#     то вивести повідомлення «немає відповідної інформації»
#     """)
# ]
#
# # цикл зі спідкуванням
# while True:
#     # Запит від користувача
#     user_query = input("Ви: ")
#
#     # умова закінчення
#     if user_query == "":
#         break
#
#     # зробити human message
#     user_message = HumanMessage(user_query)
#
#     # добавляємо повідомлення в історію
#     messages.append(user_message)
#
#     # отримати відповіть від агента
#     # агент сам дадає повідемлення в історію і повертає її
#
#     # агент треба передавати словник зі ключем "messages"
#     data = {
#         "messages": messages
#     }
#
#     data = agent.invoke(data)
#     # агент так само повертає словник
#
#     # дістаємо нову історію повідомлень
#     messages = data["messages"]
#
#     # відповідь моделі -- останнє повідомлення в історії
#     response = messages[-1]
#
#     # вивести відповідь на екран
#     print(response.text)
#
#     # виведення історії
#     print()
#     print("----------ІСТОРІЯ-----------")
#
#     for message in messages:
#         print(repr(message))  # вивести разом з назсою класу
#
#     print("-----------------------------")
#     print()

# Завдання 3
# Напишіть модель яка конвертує одну валюту в іншу за
# нинішнім курсом. Для цього напишіть функції, яка отримує
# номінал та курс і робить конвертацію.
# Практичне завдання
# Реалізуйте 2 ланцюга:
#  перший отримує назви валют та шукає курс в
# інтернеті
#  другий отримує номінал та курс і застосовує функцію
# ковертації

# ФУНКЦІЯ КОНВЕРТАЦІЇ
@tool
def converter(nominal: float, exchange: float) -> float:
    """
    Функція отримує номінал та курс і робить конвертацію

    :param nominal: номінал валюти, яку треба конвертувати
    :param exchange: курс валюти, в яку треба конвертувати
    :return: конвертована сума
    """

    print(f"Converted {nominal} by {exchange}")

    return nominal / exchange if exchange > 1 else nominal * exchange


# ПОШУК В ІНТЕРНЕТІ
@tool
def google_search(query: str):
    """
    Шукає інформацію в інтернеті

    :param query: str -- запит в пошуковик
    :return: результат пошуку
    """

    result = serper_search.results(query)

    print("\n---------- РЕЗУЛЬТАТ ПОШУКУ ----------")
    print(result)
    print("--------------------------------------\n")

    return result


# агент для пошуку курса
class GetExchange(BaseModel):
    exchange: float = Field(description="курс валюти")


# створення парсер
parser = PydanticOutputParser(pydantic_object=GetExchange)

# інструкція від парсера
instructions = parser.get_format_instructions()


# --------------------------------------------------
# АГЕНТ ДЛЯ ПОШУКУ КУРСУ
# --------------------------------------------------

agent1 = create_agent(
    model=llm,
    tools=[google_search],
)


# --------------------------------------------------
# ЦИКЛ КОНВЕРТАЦІЇ
# --------------------------------------------------

while True:

    # ----------------------------------------------
    # 1. Користувач вводить валюти
    # ----------------------------------------------

    currency = input(
        "\nВведіть валюту, яку ви хочете конвертувати: "
    )

    if currency == "":
        break

    currency_exchange = input(
        "Введіть валюту, в яку ви хочете конвертувати: "
    )

    if currency_exchange == "":
        break


    # ----------------------------------------------
    # 2. ПОШУК НОВОГО КУРСУ
    # ----------------------------------------------

    prompt1 = f"""
    Ти -- чатбот пошуку курсу валют.

    Знайди актуальний курс для конвертації:
    {currency} -> {currency_exchange}

    Використай інструмент google_search для пошуку
    актуального курсу в інтернеті.

    На основі знайденої інформації визнач курс.

    Важливо:
    - потрібен курс саме для {currency} -> {currency_exchange};
    - не використовуй старий курс;
    - якщо в пошуку курс наведений у зворотному напрямку,
      правильно перерахуй його.

    ### ФОРМАТ ВІДПОВІДІ ###
    {instructions}
    """

    data = {
        "messages": [
            HumanMessage(prompt1)
        ]
    }

    response1 = agent1.invoke(data)


    # ----------------------------------------------
    # 3. ОТРИМУЄМО ВІДПОВІДЬ АГЕНТА
    # ----------------------------------------------

    messages1 = response1["messages"]

    last_message = messages1[-1]


    # content у Gemini може бути списком
    if isinstance(last_message.content, list):
        exchange_text = last_message.content[0]["text"]
    else:
        exchange_text = last_message.content


    # ----------------------------------------------
    # 4. ПАРСИМО КУРС
    # ----------------------------------------------

    exchange_data = parser.parse(exchange_text)

    print(
        f"\nЗнайдений курс {currency} -> "
        f"{currency_exchange}: {exchange_data.exchange}"
    )


    # ----------------------------------------------
    # 5. СТВОРЮЄМО АГЕНТА КОНВЕРТАЦІЇ
    # ----------------------------------------------

    agent = create_agent(
        model=llm,
        tools=[converter],
    )


    # ----------------------------------------------
    # 6. СТВОРЮЄМО НОВУ ІСТОРІЮ
    # ----------------------------------------------

    messages = [
        SystemMessage(
            f"""
            Ти -- ввічливий чат бот.

            У тебе є доступ до інструменту:
            * converter

            ### ІНСТРУКЦІЯ ###

            1. Користувач повідомляє номінал валюти.
            2. Валюта для конвертації: {currency}
            3. Валюта, в яку потрібно конвертувати: {currency_exchange}
            4. Курс валют: {exchange_data.exchange}
            5. Виклич інструмент converter.
            6. Передай у converter номінал користувача
               та курс {exchange_data.exchange}.
            7. Поверни результат користувачу.
            8. Вкажи:
               - яку валюту в яку було конвертовано;
               - початкову суму;
               - курс;
               - результат.
            """
        )
    ]


    # ----------------------------------------------
    # 7. КОРИСТУВАЧ ВВОДИТЬ НОМІНАЛ
    # ----------------------------------------------

    user_query = input(
        f"Введіть номінал {currency}, яку хочете конвертувати: "
    )

    if user_query == "":
        break


    # ----------------------------------------------
    # 8. ДОДАЄМО ПОВІДОМЛЕННЯ
    # ----------------------------------------------

    user_message = HumanMessage(user_query)

    messages.append(user_message)


    # ----------------------------------------------
    # 9. ЗАПУСКАЄМО АГЕНТА
    # ----------------------------------------------

    data = {
        "messages": messages
    }

    data = agent.invoke(data)


    # ----------------------------------------------
    # 10. ОТРИМУЄМО НОВУ ІСТОРІЮ
    # ----------------------------------------------

    messages = data["messages"]


    # ----------------------------------------------
    # 11. ВІДПОВІДЬ МОДЕЛІ
    # ----------------------------------------------

    response = messages[-1]

    print(response.text)


    # ----------------------------------------------
    # 12. ВИВЕДЕННЯ ІСТОРІЇ
    # ----------------------------------------------

    print()
    print("---------- ІСТОРІЯ -----------")

    for message in messages:
        print(repr(message))

    print("------------------------------")



