from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pypdf import PdfReader

load_dotenv()

# Đọc PDF
reader = PdfReader("DeCuongBaiGiangBai1.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

# Kết nối Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Chatbot
while True:

    question = input("Bạn hỏi: ")

    if question.lower() == "exit":
        break

    response = llm.invoke(
        f"""
        Nội dung tài liệu:

        {text[:10000]}

        Câu hỏi:
        {question}
        """
    )

    print("\nTrả lời:")
    print(response.content)