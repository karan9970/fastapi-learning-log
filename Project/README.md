# Gemini FastAPI Demo 🚀

A simple **FastAPI + LangChain + Google Gemini** web application that demonstrates how to build an AI-powered Q&A interface using a clean UI.

This project is meant for **learning, experimentation, and interview-ready demos**.

---

## ✨ Features

* 🌐 FastAPI backend
* 🤖 Google Gemini (via LangChain)
* 🧠 Uses `gemini-2.5-flash` model
* 🎨 HTML UI with Jinja2 templates
* 📄 Form-based question input
* ⚡ Quick setup and lightweight

---

## 🛠 Tech Stack

* **Python**
* **FastAPI**
* **LangChain**
* **Google Generative AI (Gemini)**
* **Jinja2 Templates**
* **HTML / CSS**

---

## 📁 Project Structure

```
.
├── main.py              # FastAPI application
├── templates/
│   └── index.html       # UI template
├── static/              # Static files (CSS, JS)
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory and add your **Google Gemini API key**:

```
GOOGLE_API_KEY=your_api_key_here
```

> ⚠️ Do NOT commit your `.env` file to GitHub.

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/karan9970/fastapi-learning-log
cd https://github.com/karan9970/fastapi-learning-log
```

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the FastAPI server

```bash
uvicorn main:app --reload
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000
```

---

## 🧠 How It Works

1. User enters a question in the web UI
2. FastAPI receives the form submission
3. LangChain sends the prompt to **Gemini**
4. Gemini generates a response
5. The answer is rendered back in the UI

---

## 📌 Example Code Snippet

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0
)

result = llm.invoke(question)
answer = result.content
```

---

## 🚧 Future Improvements

* Add streaming responses
* Chat history support
* Better UI styling
* Error handling & validation
* Model selection toggle

---

## 🎯 Use Case

* AI learning projects
* LangChain + Gemini demos
* FastAPI interview showcase

This project is open-source and free to use for learning and experimentation.

### ⭐ If you like this project, give it a star!
