from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Đọc PDF
reader = PdfReader("DeCuongBaiGiangBai1.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

# Chia nhỏ văn bản
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(text)

print("Số chunks:", len(chunks))

# Embedding
model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(chunks)

# Tạo FAISS Index
dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors).astype("float32"))

# Lưu index
faiss.write_index(index, "faiss_index.bin")

# Lưu chunks
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Đã tạo faiss_index.bin và chunks.pkl")