# Завдання 1
# Напишіть модель для генерації персонального плану
# тренувань з двох ланцюгів:
#  Перший ланцюг отримує мету тренування(схуднення,
# набір м’язів, тощо) та повертає список вправ
#  Другий ланцюг отримує список вправ, рівень
# підготовки користувача(низький, середній,
# професіонал) та кількість часу на тиждень(в годинах)
# і повертає план тренувань

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
class Exercises(BaseModel):
    exercises: list[str] = Field(description="перелік вправ")

# створення парсер
parser1 = PydanticOutputParser(pydantic_object=Exercises)

# інструкція від парсера
instruсtions = parser1.get_format_instructions()

# промпт
prompt1 = PromptTemplate.from_template("""
    Ти -- спортивний тренер.
    Твоя задача отримати від користувача мету тренування (наприклад, схуднення,
    набір м’язів, тощо)
    та визначити перелік найбільш ефективних для досягнення цієї мети вправ

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instruсtions}

    ###ВХІДНІ ДАНІ###
    Мета: {goal}
""",
   partial_variables={"format_instruсtions": instruсtions}
   # оодразу передає інструкції від парсера
)

# # ланцюг для першого кроку
chain1 = prompt1 | llm | parser1


# крок 2
# згенерувати план тренування для досягнення мети

class TrainingPlan(BaseModel):
    plan: str = Field(description="план тренування, для досягнення мети")


parser2 = PydanticOutputParser(pydantic_object=TrainingPlan)

instruсtions = parser2.get_format_instructions()

# промпт

prompt = PromptTemplate.from_template("""
    Ти -- спортивний тренер.
    Твоя задача отримати перелік вправ, рівень підготовки користувача(низький, середній, професіонал)
    та кількість часу на тиждень(в годинах) і надати план тренування, виходячи з рекомендованих вправ.

    ###ІНСТРУКЦІЇ###
    1. план тренування має дотримуватися рівня підготовки, не перевантажити
    2. надати загальні рекомендації, що щроблять тренування більш ефективним та безпечним (наприклад, пити воду) 

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}

    ###ВХІДНІ ДАНІ###
    Перелік вправ: {exercises}
    Рівень підготовки: {level}
    Час на тиждень: {time}
""",
partial_variables={"format_instructions": instruсtions}
)

# ланцюг для кроку 2

chain2 = prompt | llm | parser2

# використання

user_input = input("введіть мету тренування ")

data = {
    "goal": user_input,
}

# запускаємо перший ланцюг

response1 = chain1.invoke(data)

print("Перелік вправ:")
for exercise in response1.exercises:
    print(exercise)

# # дані для другого ланцюга

level = input("введіть ваш рівень підготовки: низький, середній, професіонал ... ")
time = input("введіть час тренувань на тиждень (в годинах) ")

data = {
    "exercises": response1.exercises,
    "level": level,
    "time": time
}

# запускаємо другий ланцюг
response2 = chain2.invoke(data)

print(f"Рекомендований План тренування: {response2.plan}")
