import dotenv
import os

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


from pydantic import BaseModel, Field

# завантажити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# # модель
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # назва моделі
    api_key=api_key  # ключ до сервера з моделлю
)

class Response(BaseModel):
    words: list[str] = Field(description= "список унікальних англійських слів")

parser = PydanticOutputParser(pydantic_object=Response)

instructions = parser.get_format_instructions()

prompt = PromptTemplate.from_template("""

    Твоя задача дістати унікальні тільки англійськи слова з тексту

    ###ІНСТРУКЦІЇ###
    1. ігноруй артиклі
    2. ігноруй стоп слова (is, are, is, it, as  тощо)
    3. НІКОЛИ не додавай українські слова.
    4. Не додавай одне слово більше одного разу.


    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}
    
    ###ВХІДНІ ДАНІ###
    {text}

""",
partial_variables={"format_instructions": instructions}
)

# ланцюг

chain = prompt | llm | parser


if __name__ == "__main()__":

    text = """I am reading a book. — Я читаю книгу. She bought a new book yesterday. — Вона вчора купила нову книгу."
            "I want to book a hotel room. — Я хочу забронювати номер у готелі."
            "We booked a flight to London. — Ми забронювали рейс до Лондона."""

    data = {
        "text": text
    }

    response = chain.invoke(data)

    print(response)

