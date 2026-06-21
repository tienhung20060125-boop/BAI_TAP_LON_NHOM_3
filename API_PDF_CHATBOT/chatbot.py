from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Đọc API Key
load_dotenv()

# Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS
index = faiss.read_index("faiss_index.bin")

# Load chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

print("=== PDF CHATBOT ===")
print("Gõ 'exit' để thoát\n")

while True:

    question = input("Bạn hỏi: ")

    if question.lower() == "exit":
        break

    # Embedding câu hỏi
    question_vector = model.encode([question])

    # Tìm 3 chunk liên quan nhất
    D, I = index.search(
        np.array(question_vector).astype("float32"),
        k=3
    )

    context = ""

    for idx in I[0]:
        context += chunks[idx]
        context += "\n\n"

    # Prompt gửi Gemini
    prompt = f"""
    Dựa vào nội dung tài liệu dưới đây:

    {context}

    Hãy trả lời câu hỏi:

    {question}

    Nếu tài liệu không chứa câu trả lời thì nói rõ.
    """

    response = llm.invoke(prompt)

    print("\nTrả lời:")
    print(response.content)
    print("\n" + "="*50 + "\n")