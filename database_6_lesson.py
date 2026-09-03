# пошук потрібного документа
# RAG -- (пошук - відповідь - генерація)

# документ1 -- Суп корисний при застуді
# документ2 -- Суп придумали в Китаї
# документ3 -- Наша компанія знаходиться в Миколаєві


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

index_name = "itset-docs"  # назва бази даних

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

# документ1 -- Суп корисний при застуді
doc1 = Document(
    page_content="Суп корисний при застуді",
)

# документ2 -- Суп придумали в Китаї
doc2 = Document(
    page_content="Суп придумали в Китаї",
)

# документ3 -- Наша компанія знаходиться в Миколаєві
doc3 = Document(
    page_content="Наша компанія знаходиться в Миколаєві",
)

# створення ілентифікаторів
documents = [doc1, doc2, doc3]
uuids = [str(uuid4()) for _ in range(len(documents))]

# # добавити документи в базу даних
# vector_store.add_documents(
#     documents=documents,
#     ids=uuids
# )


# знаходження сходих документів

user_query = "де наша компанія"

results = vector_store.similarity_search(
    user_query,   # текст для пошуку схожих документів
    k=2,          # кількість документів яку шукаємо
)

for doc in results:
    print(doc.page_content)