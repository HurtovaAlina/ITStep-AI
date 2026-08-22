# Завдання 1
# Напишіть промпт для створення плану навчального
# курсу з певної теми для цільової айдиторії(початківці,
# професіонали, діти, тощо).
# Вхідні параметри: тема, опис цільової аудиторії
# Реалізуйте двома способами:
#  Zero-shot
#  Few-shot

import dotenv
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# # модель
llm = GoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key,  # ключ до сервера з моделлю
    temperature = 0.3
)

#Zero-Shot — без прикладів
prompt = PromptTemplate.from_template("""
    Ти -- менеджер ІТ школи.
    Твоя задача створити план навчального курсу з визначеної теми для певної цільової айдиторії(початківці,
професіонали, діти, тощо).

    ###ВХІДНІ ДАНІ###
    ТЕМА: {topic}
    АУДИТОРІЯ: {audience}
"""
                                      )

topic = input("Введіть тему, для якої треба створити програму курсу ")
audience = input("Введіть цільову аудиторію, для якої буде цей курс:\n"
                 "початківці,\n"
                 "професіонали,\n"
                 "діти\n")

chain = prompt | llm
# спочатку формується повний текст на вхід моделі
data = {
    "topic": topic,
    "audience": audience
}
response = chain.invoke(data)

print("Zero-Shot example")
print(response)

#  Few-shot
prompt = PromptTemplate.from_template("""
    Ти -- менеджер ІТ школи.
    Твоя задача створити план навчального курсу з визначеної теми для певної цільової айдиторії(початківці,
професіонали, діти, тощо).

    ###ІНСТРУКЦІЯ###:
    Враховуй рівень підготовки аудиторії.
    Розташовуй теми від простих до складних.
    Для дітей треба знайти такі теми, що можуть зацікавити дітей, відповідно віку. 
    Для професіоналів роби акцент на сучасних технологіях, практичному застосуванні та production-сценаріях.
    
    ###ПРИКЛАД###
    Тема: Python
    Аудиторія: діти
    
    Модуль 1. Знайомство з програмуванням
    ......
    Модуль 2. Змінні та типи даних

    Тема: ШІ
    Аудиторія: професіонали
    
    Модуль 1. Сучасний ландшафт штучного інтелекту
    ..........
    Модуль 2. AI-агенти
    ..........
    Модуль 3. Multi-Agent Systems
    
    ###ВХІДНІ ДАНІ###
    ТЕМА: {topic}
    АУДИТОРІЯ: {audience}
""")


chain = prompt | llm
# спочатку формується повний текст на вхід моделі
data = {
    "topic": topic,
    "audience": audience
}
response = chain.invoke(data)

print("Few-shot example")
print(response)
