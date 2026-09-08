# Завдання 1
# Напишіть додаток, який симулює спілкування з певною
# відомою людиною.
# З ким саме спілкуватись вводить користувач через
# st.text_input()

#streamlit run practice_7_UI.py

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
        SystemMessage("""
        Ти -- ввічливий чатбот, який симулює певну відому людину
        Користувач задає відому людину.
        Твоя задача підтримувати діалог з користувачем, симулюючи спілкування користувача з цією відомою людиною

        """)
    ]


# заголовок
st.title("Наш чатбот")

# отримати повідомлення від користувача
user_text = st.chat_input("Введіть повідомлення")

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

# Завдання 2
# Напишіть додаток, який симулює проходження
# співбесіди на певну посаду.
# Користувач може ввести назву посади через st.text_input()
# Користувач може ввести опис вакансії через
# st.file_uploader()
# Далі починається чат з спілкуванням


# Завдання 3
# Напишіть чат бота з доступом до інтернету