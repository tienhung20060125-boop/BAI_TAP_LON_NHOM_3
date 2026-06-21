from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI PDF Assistant</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    display:flex;
    height:100vh;
    background:#0b1120;
    color:white;
}

/* Sidebar */

.sidebar{
    width:260px;
    background:#111827;
    border-right:1px solid #1f2937;
    padding:20px;
}

.sidebar h2{
    margin-bottom:30px;
}

.sidebar button{
    width:100%;
    padding:14px;
    margin-top:10px;
    border:none;
    border-radius:12px;
    background:#1f2937;
    color:white;
    cursor:pointer;
    transition:.3s;
}

.sidebar button:hover{
    background:#2563eb;
}

/* Main */

.main{
    flex:1;
    display:flex;
    flex-direction:column;
}

/* Header */

.header{
    text-align:center;
    padding:50px 20px 20px;
}

.header h1{
    font-size:60px;
    margin-bottom:10px;
}

.header p{
    color:#94a3b8;
    font-size:18px;
}

/* Chat */

.chat{
    flex:1;
    overflow-y:auto;
    padding:20px 40px;
}

.message{
    max-width:70%;
    padding:15px;
    border-radius:18px;
    margin-bottom:15px;
    line-height:1.6;
}

.bot{
    background:#1e293b;
}

.user{
    background:#2563eb;
    margin-left:auto;
}

/* Input */

.input-area{
    padding:20px;
    border-top:1px solid #1f2937;
    display:flex;
    gap:12px;
    align-items:center;
}

.input-area input{
    flex:1;
    padding:16px;
    border:none;
    border-radius:15px;
    font-size:16px;
    outline:none;
}

.send-btn{
    padding:16px 25px;
    border:none;
    border-radius:15px;
    background:#2563eb;
    color:white;
    cursor:pointer;
}

.send-btn:hover{
    background:#1d4ed8;
}

/* Voice */

.voice-btn{
    width:50px;
    height:50px;
    min-width:50px;
    border:none;
    border-radius:50%;
    background:#1f2937;
    color:white;
    cursor:pointer;
    display:flex;
    justify-content:center;
    align-items:center;
    transition:.3s;
}

.voice-btn:hover{
    background:#374151;
    transform:scale(1.05);
}

</style>
</head>

<body>

<div class="sidebar">

<h2>🤖 AI PDF</h2>

<button>📄 Upload PDF</button>

<button>💬 Chat History</button>

</div>

<div class="main">

<div class="header">
<h1>AI PDF Assistant</h1>
<p>Đọc PDF • Hỏi đáp • Voice Chat</p>
</div>

<div class="chat">

<div class="message bot">
👋 Xin chào, tôi có thể hỗ trợ đọc tài liệu PDF.
</div>

</div>

<div class="input-area">

<button class="voice-btn">

<svg width="20" height="20" viewBox="0 0 24 24" fill="none">
<path d="M12 15C14.2 15 16 13.2 16 11V5C16 2.8 14.2 1 12 1C9.8 1 8 2.8 8 5V11C8 13.2 9.8 15 12 15Z"
fill="white"/>
<path d="M19 11C19 15 15.9 18 12 18C8.1 18 5 15 5 11"
stroke="white"
stroke-width="2"
stroke-linecap="round"/>
<path d="M12 18V23"
stroke="white"
stroke-width="2"
stroke-linecap="round"/>
</svg>

</button>

<input type="text" placeholder="Nhập câu hỏi...">

<button class="send-btn">Gửi</button>

</div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)