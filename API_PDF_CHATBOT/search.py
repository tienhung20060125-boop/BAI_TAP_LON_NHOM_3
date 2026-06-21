from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load index
index = faiss.read_index("faiss_index.bin")

# Load chunks
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Nhập câu hỏi
question = input("Câu hỏi: ")

# Embedding câu hỏi
question_vector = model.encode([question])

# Tìm 3 đoạn liên quan nhất
D, I = index.search(
    np.array(question_vector).astype("float32"),
    k=3
)

print("\n=== Kết quả ===")

for idx in I[0]:
    print("\n------------------")
    print(chunks[idx])