# пошук потрібного документа
# RAG -- (пошук - відповідь - генерація)


import dotenv
import os


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from uuid import uuid4
from pinecone import ServerlessSpec
from pinecone import Pinecone

# завантадити дані з .env
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# модель для преведення текстів у вектори(набір чисел)
embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key,
)

# # переветення тексту у вектор
# text1 = "Суп корисний при застуді"
# vector1 = embedding.embed_query(text1)
#
# print(vector1)
# print(type(vector1))
# print(len(vector1))
#
# # текст 2
# text2 = "Суп"
# vector2 = embedding.embed_query(text2)
#
# print(vector2)

# векторна база даних
pc = Pinecone(api_key=pinecone_api_key)

# створення бази даних

index_name = "text-docs"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=3072,    # кількість чисел у векторі
        metric="cosine",   # формула для пошуку схожих текстів
        spec=ServerlessSpec(
            cloud="aws",        # хмарна платформа(амазон)
            region="us-east-1"  # регіон
        ),
    )

index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,          # база даних
    embedding=embedding   # модель для кодування
)


# добавити тексти
# обробка попередня


# документ1 -- future_of_ai
with open("data/lesson_rag/files/future_of_ai.txt", "r", encoding="utf-8") as f:
    future_of_ai = f.read()
    # print(future_of_ai)

doc1 = Document(
    page_content=future_of_ai,
)

# документ2 -- intro
with open("data/lesson_rag/files/intro.txt", "r", encoding="utf-8") as f:
    intro = f.read()

doc2 = Document(
    page_content=intro,
)

# документ3 -- machine_learning
with open("data/lesson_rag/files/machine_learning.txt", "r", encoding="utf-8") as f:
    machine_learning = f.read()

doc3 = Document(
    page_content=machine_learning,
)

# документ4 -- neural_networks
with open("data/lesson_rag/files/neural_networks.txt", "r", encoding="utf-8") as f:
    neural_networks = f.read()

doc4 = Document(
    page_content=neural_networks,
)

# створення ілентифікаторів
documents = [doc1, doc2, doc3, doc4]
uuids = [str(uuid4()) for _ in range(len(documents))]

# добавити документи в базу даних
vector_store.add_documents(
    documents=documents,
    ids=uuids
)

