
import streamlit as st

# # на фоні працює цикл while True
# # заголовок сайту
# st.title("Наш сайт для чат бота")
#
#
# # звичайний текст
# st.markdown("Сьогодні останнє заняття по роботі з чат ботами та llm")
#
# # # історія повідомлень
# # history = []
#
# # отримати повідомлення від користувача
# user_text = st.chat_input("Запийте чат бота щось")
#
# # history.append(user_text)
# #
# # print(f"{history = }")
#
#
#
# # глобальна пам'ять в streamlit
#
# # якщо історії ще немає то створюємо порожній список(перший запуск)
# if "history" not in st.session_state:
#     #st.session_state["history"] = []
#     st.session_state.history = []
#
# st.session_state.history.append(user_text)
#
# print(f"{st.session_state.history = }")
#
# # результати
# st.markdown(f"ви сказали {user_text}")

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
        Ти -- ввічливий чатбот
        Твоя задача підтримувати спілкування з користувач
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