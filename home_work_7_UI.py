# Завдання 1
# Напишіть додаток з чат ботом по допомозі з вивченням
# англійської мови.
#  Якщо користувач просить перекласти слово або
# фразу, то вивести переклад та приклад використання
# у речені
#  Якщо користувач просить перекласти речення, то
# вивести переклад та пояснення граматики, наприклад
# структура there is/are, пасивна форма дієслова, тощо

#streamlit run

import streamlit as st

# ЧАТ-БОТ

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    BaseMessage,
    trim_messages,
)

# завантадити дані з .env
api_key = st.secrets["GEMINI_API_KEY"]


# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

# # # історія повідомлень

if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(f"""
        Ти -- чатбот - вчитель англійскої мови.
        Твоя задача підтримувати діалог з користувачем, допомагаючи йому у вивченні англійскої мови
        ###ІНСТРУКЦІЇ###
        Якщо користувач просить перекласти слово або фразу, то вивести переклад та приклад використання
        у речені
        Якщо користувач просить перекласти речення, то вивести переклад та пояснення граматики, наприклад
        структура there is/are, пасивна форма дієслова, тощо
    """)
    ]

# заголовок
st.title("ENGLISH TEACHER")

user_text = st.chat_input("Enter your question")

# якщо повідомлення не None тоді викликаємо чат бот
if user_text is not None:
    # створити HumanMessage
    human_message = HumanMessage(content=user_text)

    # отримати історію повідомлень
    messages = st.session_state.history

    # додати повідемлення в історії
    messages.append(human_message)

    # отримати відповідь моделі
    response = llm.invoke(messages)

    # добавити response в історію спілкування
    messages.append(response)

    # вивести всю історію повідомлень
    for message in messages:
        # не показувати SystemMessage
        if isinstance(message, SystemMessage):
            continue

        # отримуємо тип повідомлення
        role = ""
        if isinstance(message, HumanMessage):
            role = "user"
        else:
            role = "AI"

        with st.chat_message(role):  # добавляємо іконку до повідомлення
            st.markdown(message.text)