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

# структура відповіді
class BookPlot(BaseModel):
    plot: str = Field(description="жанр книги")


# створення парсер
parser1 = PydanticOutputParser(pydantic_object=BookPlot)

# інструкція від парсера
instruсtions = parser1.get_format_instructions()

# промпт
prompt1 = PromptTemplate.from_template("""
    Ти -- бібліотекар.
    Твоя задача отримати від користувача назву книги 
    та визначити жанр книги

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instruсtions}

    ###ВХІДНІ ДАНІ###
    Книга: {book}
""",
   partial_variables={"format_instruсtions": instruсtions}
   # оодразу передає інструкції від парсера
)

# ланцюг для першого кроку
chain1 = prompt1 | llm | parser1

# використання
user_input = "Гаррі Поттер і філософський камінь"

data = {
    "book": user_input,
}


# крок 2
# згенерувати перелік книг по визначеній темі

class Reccomended_Books(BaseModel):
    books: list[str] = Field(description="список книг, заданого жанру")


parser2 = PydanticOutputParser(pydantic_object=Reccomended_Books)

instruсtions = parser2.get_format_instructions()

# промпт

prompt = PromptTemplate.from_template("""
    Ти -- бібліотекар.
    Твоя задача надати перелік книг заданого жанру.

    ###ІНСТРУКЦІЇ###
    1. Не більше 3 книг
    2. Надай назву книги та автора

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}

    ###ВХІДНІ ДАНІ###
    Жанр: {plot}
""",
partial_variables={"format_instructions": instruсtions}
)

# ланцюг для кроку 2

chain2 = prompt | llm | parser2

# # використання
#
# user_input = "Гаррі Поттер і філософський камінь"

# дані для першого ланцюга
data = {
    "book": user_input
}

# запускаємо перший ланцюг

response1 = chain1.invoke(data)

print(f":Жанр: {response1.plot}")

# # дані для другого ланцюга
data = {
    "plot": response1.plot
}

# запускаємо другий ланцюг
response2 = chain2.invoke(data)

print(f"Книги заданого жанру {response1.plot}:")
for book in response2.books:
    print(book)


# Завдання 2
# Напишіть модель для генерації листа:
#  Перший ланцюг отримує короткий опис листа та
# генерує основний зміст
#  Другий ланцюг отримує основний зміст та стиль
# листа(формальний, неформальний, тощо) та генерує
# лист
# Завдання 3
# Напишіть модель для генерації резюме:
#  Перший ланцюг отримує опис вакансії та повертає
# основні навички, які необхідні
#  Другий ланцюг отримує основні навички та опис
# кандидата і генерує резюме