# Завдання 1
# Напишіть модель для рекомендації книг з двох ланцюгів:
#  Перший ланцюг отримує назву книги та визначає її
# жанр
#  Другий отримує назву книги, жанр та повертає список
# схожих книг(того ж самого жанру та іншого)

import dotenv
import os

import langchain
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

# # структура відповіді
# class BookPlot(BaseModel):
#     plot: str = Field(description="жанр книги")
#
#
# # створення парсер
# parser1 = PydanticOutputParser(pydantic_object=BookPlot)
#
# # інструкція від парсера
# instruсtions = parser1.get_format_instructions()
#
# # промпт
# prompt1 = PromptTemplate.from_template("""
#     Ти -- бібліотекар.
#     Твоя задача отримати від користувача назву книги
#     та визначити жанр книги
#
#     ###ФОРМАТ ВІДПОВІДІ###
#     {format_instruсtions}
#
#     ###ВХІДНІ ДАНІ###
#     Книга: {book}
# """,
#    partial_variables={"format_instruсtions": instruсtions}
#    # оодразу передає інструкції від парсера
# )
#
# # ланцюг для першого кроку
# chain1 = prompt1 | llm | parser1
#
# # використання
# user_input = "Гаррі Поттер і філософський камінь"
#
# data = {
#     "book": user_input,
# }
#
#
# # крок 2
# # згенерувати перелік книг по визначеній темі
#
# class Reccomended_Books(BaseModel):
#     books: list[str] = Field(description="список книг, заданого жанру")
#
#
# parser2 = PydanticOutputParser(pydantic_object=Reccomended_Books)
#
# instruсtions = parser2.get_format_instructions()
#
# # промпт
#
# prompt = PromptTemplate.from_template("""
#     Ти -- бібліотекар.
#     Твоя задача надати перелік книг заданого жанру.
#
#     ###ІНСТРУКЦІЇ###
#     1. Не більше 3 книг
#     2. Надай назву книги та автора
#
#     ###ФОРМАТ ВІДПОВІДІ###
#     {format_instructions}
#
#     ###ВХІДНІ ДАНІ###
#     Жанр: {plot}
# """,
# partial_variables={"format_instructions": instruсtions}
# )
#
# # ланцюг для кроку 2
#
# chain2 = prompt | llm | parser2
#
# # # використання
# #
# # user_input = "Гаррі Поттер і філософський камінь"
#
# # дані для першого ланцюга
# data = {
#     "book": user_input
# }
#
# # запускаємо перший ланцюг
#
# response1 = chain1.invoke(data)
#
# print(f":Жанр: {response1.plot}")
#
# # # дані для другого ланцюга
# data = {
#     "plot": response1.plot
# }
#
# # запускаємо другий ланцюг
# response2 = chain2.invoke(data)
#
# print(f"Книги заданого жанру {response1.plot}:")
# for book in response2.books:
#     print(book)


# Завдання 2
# Напишіть модель для генерації листа:
#  Перший ланцюг отримує короткий опис листа та
# генерує основний зміст
#  Другий ланцюг отримує основний зміст та стиль
# листа(формальний, неформальний, тощо) та генерує
# лист

# # структура відповіді
# class LetterContent(BaseModel):
#     letter_content: str = Field(description="основний зміст листа")
#
#
# # створення парсер
# parser1 = PydanticOutputParser(pydantic_object=LetterContent)
#
# # інструкція від парсера
# instructions = parser1.get_format_instructions()
#
# # промпт
# prompt1 = PromptTemplate.from_template("""
#     Ти -- чатбот по написанню листів.
#     Твоя задача на підставі короткого опису листа згенерувати основний зміст
#
#     ###ІНСТРУНКЦІЇ###
#     1. Відповідь має містити основний зміст, викладений до 2 речень
#
#
#     ###ФОРМАТ ВІДПОВІДІ###
#     {format_instructions}
#
#     ###ВХІДНІ ДАНІ###
#     Опис листа: {letter_description}
# """,
#    partial_variables={"format_instructions": instructions}
#    # оодразу передає інструкції від парсера
# )
#
# # ланцюг для першого кроку
# chain1 = prompt1 | llm | parser1
#
# # використання
# letter_description = """
# Напиши листа колезі з подякою за допомогу у виконанні
# важливого робочого завдання. Повідом, що завдяки його допомозі
# проєкт було успішно завершено.
# """
#
# data = {
#     "letter_description": letter_description,
# }
#
# # крок 2
# # згенерувати лист визначеного стилю
#
# class Letter(BaseModel):
#     style: str = Field(description="стиль листа (формальний, неформальний, тощо)")
#     letter: str = Field(description="лист")
#
#
# parser2 = PydanticOutputParser(pydantic_object=Letter)
#
# instructions = parser2.get_format_instructions()
#
# # промпт
#
# prompt = PromptTemplate.from_template("""
#     Ти -- чатбот по написанню листів.
#     Твоя задача підставі бажаного стилю  і основного змісту листа згенерувати лист
#
#     ###ІНСТРУКЦІЇ###
#     1. Лист має бути дотриманий бажаного стилю
#     2. Не більше 7 речень
#     3. Ввічливим
#
#     ###ФОРМАТ ВІДПОВІДІ###
#     {format_instructions}
#
#     ###ВХІДНІ ДАНІ###
#     Стиль: {style}
#     Основний зміст: {letter_content}
# """,
# partial_variables={"format_instructions": instructions}
# )
#
# # ланцюг для кроку 2
#
# chain2 = prompt | llm | parser2
#
# # використання
#
# style = "формальний"
#
# # дані для першого ланцюга
# data = {
#     "letter_description": letter_description
# }
#
# # запускаємо перший ланцюг
#
# response1 = chain1.invoke(data)
#
# print(f"Основний зміст листа: {response1.letter_content}")
#
# # # дані для другого ланцюга
# data = {
#     "style": style,
#     "letter_content": response1.letter_content
# }
#
# # запускаємо другий ланцюг
# response2 = chain2.invoke(data)
#
# print(f"Готовий лист заданого стилю {style}:")
# print(response2)

# Завдання 3
# Напишіть модель для генерації резюме:
#  Перший ланцюг отримує опис вакансії та повертає
# основні навички, які необхідні
#  Другий ланцюг отримує основні навички та опис
# кандидата і генерує резюме

# структура відповіді
class Skills(BaseModel):
    other_skills: list[str] = Field(description="перелік інших навичок")
    english_level: str = Field(description="рівень англійської мови")
    frameworks: list[str] = Field(description="фреймворки")
    experience: int = Field(description="досвід в роках")
    technologies: list[str] = Field(description="список технологій")
    programming_language: str =Field(description="мова програмування")


# створення парсер
parser1 = PydanticOutputParser(pydantic_object=Skills)

# інструкція від парсера
instructions = parser1.get_format_instructions()

# промпт
prompt1 = PromptTemplate.from_template("""
    Ти -- досвідчений рекрутер.
    Твоя задача на підставі отриманої вакансії обрати основні навички, що потрібні для даної вакансії

    ###ІНСТРУНКЦІЇ###
    1. всі навички треба розподілити відповідно: фреймворки, тенології, тощо
    2. якщо не знаєш куди віднести навичку, додавай її до інших навичок

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}

    ###ВХІДНІ ДАНІ###
    Вакансія: {position}
""",
partial_variables={"format_instructions": instructions}
# оодразу передає інструкції від парсера
)

# ланцюг для першого кроку
chain1 = prompt1 | llm | parser1

# використання
position = """We are looking for a passionate Data Scientist to implement AI solutions aimed at achieving business goals.

This role offers the opportunity to work on cutting-edge AI adoption projects that helps to improve current business processes.
You'll be a great fit if you have:
Strong Python Experience (2 year +);
Experience with LLM , Diffusion models;
Knowledge of Prompt engineering;
Experience with Gen AI-related technologies such as LangChain and RAG;
Experience with Neural Networks (Optional) ;
Experience with NLP , Predictive analytics and Machine learning;
Experience with Pandas;
Experience with SQL, including experience with large datasets;
Strong experience in statistics;
Bachelor's degree in Computer Science or a related field.
What you'll do:
Develop AI agents that utilize LLM, RAG and langchain approach;
Implement LLM and Diffusion models to boost business productivity;
Utilize LLM (LLM Vision) to improve object detection, text classification and extraction;
Create forecasting, recommendation, and classification models;
Transform business challenges to AI applications.

We ensure your growth with:
Competitive salary fixed in USD;
Flexible working schedule and fully remote work format;
Paid vacation days and sick leave days ;
Personal and professional development opportunities;
Participation in building innovative projects from scratch using modern technologies;
Team-building activities and corporate events;
English classes and educational events."""

data = {
    "position": position,
}

# запускаємо перший ланцюг

response1 = chain1.invoke(data)

print(f"Основні навички: "
      f"Мова програмування {response1.programming_language}\n"
      f"Технології {response1.technologies}\n"
      f"Досвід {response1.experience} роки\n"
      f"Фреймворки {response1.frameworks}\n"
      f"Рівень англійської {response1.english_level}\n"
      f"Інші навички {response1.other_skills}\n"
      )

# крок 2
# згенерувати резюме

class CV(BaseModel):
    cv: str = Field(description="резюме")


parser2 = PydanticOutputParser(pydantic_object=CV)

instructions = parser2.get_format_instructions()

# промпт

prompt = PromptTemplate.from_template("""
    Ти -- досвідчений помічник в складанні резюме.
    Твоя задача на підставі опису кандидата і наданих навичок скласти цікаве резюме

    ###ІНСТРУКЦІЇ###
    1. крім навичок резюме має містити опис кандидата, мотиваційний зміст
    2. вказати 3-5 софт скіллів

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}

    ###ВХІДНІ ДАНІ###
    опис кандидата: {applicant_description}
    перелік інших навичок: {other_skills} 
    рівень англійської мови: {english_level}
    фреймворки: {frameworks}
    досвід в роках: {experience}
    список технологій:{technologies}
    мова програмування: {programming_language}
""",
partial_variables={"format_instructions": instructions}
)

# ланцюг для кроку 2

chain2 = prompt | llm | parser2

# використання

applicant_description = """Кандидат має 3 роки досвіду роботи з аналізом даних і машинним навчанням. 
Володіє Python, SQL, Pandas, Scikit-learn та TensorFlow. Має досвід створення моделей 
прогнозування, обробки великих обсягів даних і візуалізації результатів. 
Шукає вакансію Data Scientist у міжнародній компанії."""


# # дані для другого ланцюга
data = {
    "applicant_description" :applicant_description,
    "programming_language": response1.programming_language,
    "technologies": response1.technologies,
    "experience": response1.experience,
    "frameworks": response1.frameworks,
    "english_level": response1.english_level,
    "other_skills": response1.other_skills
}

# запускаємо другий ланцюг
response2 = chain2.invoke(data)

print(f"Резюме:")
print(response2)