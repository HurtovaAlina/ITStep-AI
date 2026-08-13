# завантеження api key як змінну середовища
import dotenv
import os


import langchain
from langchain_google_genai import GoogleGenerativeAI

# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# print(api_key)

llm = GoogleGenerativeAI(
    model="gemini-3.6-flash",   # назва моделі
    api_key=api_key,    # ключ до сервера з моделлю
    temperature =1.9, # температура впливає на креативність, чим більша креативність, тим більше температура
    top_p=0.8,
    top_k=10

)
print(langchain.__version__)
#використання
response =llm.invoke("Придумай коротку існорію про ельфа (до 6 речень)")
print(response)

# параметри генерації
