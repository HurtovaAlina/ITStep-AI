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