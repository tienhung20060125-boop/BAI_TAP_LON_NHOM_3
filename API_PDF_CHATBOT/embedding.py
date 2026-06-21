from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

vector = model.encode("Trí tuệ nhân tạo là gì?")

print(len(vector))
print(vector[:10])