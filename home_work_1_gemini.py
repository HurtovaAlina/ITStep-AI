# Завдання 1
# Прочитайте файл data\lesson9\return_policy.txt Та
# напишіть простий чат бот для відповідей на питання
# користувачів стосовно повернення товару. Діалог завершується
# коли користувач вводить порожній рядок.
# Передавайте усю історію спілкування у форматі:
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:

import dotenv
import os

from langchain_google_genai import GoogleGenerativeAI

# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(
    model="gemini-3.5-flash-lite",   # назва моделі
    api_key=api_key,    # ключ до сервера з моделлю
)

with open("data/lesson9/return_policy.txt", encoding ="utf-8") as file:
    policy = file.read()
    # print(policy)

    questions = []
    responses = []

    instructions = f"""прочитай політику повернення товару, збережену в {policy}
        прочитай питання  користувача,
        і знайдаи відповідь стосовно повернення товару в політиці, з посиланням на пункт політики. Якщо відповіді
        немає в політиці, не вигадуй, а напиши, що не передбачена така ситуація діючою політикою, але якщо це 
        передбачено законодавством України, надай відповідь з посиланням на статтю чинного Закону України.
    """

    while True:
        question = input("Введіть запитання щодо повернення товару ")
        if question == "":
            print("chat is finished")
            break

        history = ""

        for old_question, old_response in zip(questions, responses):
            history += f"\nUser: {old_question}"
            history += f"\nModel: {old_response}"

        chat = f"""
        {instructions}

        Історія спілкування:
        {history}
        User: {question}
        Model:
        """

        response = llm.invoke(chat)

        print(f"Відповідь: {response}")

        questions.append(question)
        responses.append(response)
    # показати історію
    print("==== HISTORY =====")

    history = ""

    for question, response in zip(questions, responses):
        history += f"\nUser: {question}"
        history += f"\nModel: {response}"

    print(history)