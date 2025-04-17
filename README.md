# 🤖 AI-Powered Chatbot Using Django & Gemini API

## 📘 Project Overview

This is a smart **AI chatbot web application** developed using **Django** as the backend framework and **Gemini API** for natural language understanding. The chatbot accepts both **text** and **voice input** from users and responds in real-time using AI-generated replies.

> This project demonstrates integration between frontend UI, Django backend, and external LLM APIs like Gemini.

---

## 🔄 Execution Flow

### 1. **User Interaction**
- The user can type or speak their query using the voice-to-text mic button.
- The `SpeechRecognition API` converts speech to text and fills the input box.

### 2. **Frontend to Backend**
- When the user clicks the **Send** button, JavaScript uses **AJAX** (`jQuery`) to send the message to the Django backend (`/get_response/` endpoint).

### 3. **Backend Processing**
- The Django view receives the input message.
- It sends this message to **Gemini API** for processing.
- Gemini responds with a generated reply (answer, info, or code).

### 4. **Frontend Response Handling**
- Django returns the AI's response to the frontend.
- JavaScript displays it in the chatbox.
- The chat auto-scrolls to show the latest messages.

---

## 🧠 Technologies Used

| Layer         | Tech Stack                              |
|---------------|------------------------------------------|
| Frontend      | HTML, CSS, JavaScript, jQuery            |
| Backend       | Python, Django Framework                 |
| AI/LLM        | Gemini API (Generative AI for chat)      |
| Speech Input  | Web Speech API (Voice Recognition)       |
| Database (Optional) | SQLite / MySQL for saving history |

---

## ✨ Features

- ✅ Real-time chat with AI using Gemini
- 🎤 Voice-to-text input with mic button
- 📱 Responsive and clean UI
- 🔐 CSRF-protected AJAX requests
- 💬 Auto-scroll chatbox
- 📁 Easily extendable to store chat history, user login, etc.

---

## 🚀 How to Run the Project

1. **Clone the Repo**  
   ```bash
   git clone https://github.com/your-username/chatbot.git
   cd chatbot
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
python manage.py runserver
Open in Browser Visit: http://127.0.0.1:8000
