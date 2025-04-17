# chatbot
# 🤖 Chatbot Using Django + Gemini API

## 💡 Project Description
This is an AI-powered chatbot built using Django, Gemini API, HTML, CSS, and JavaScript. It supports voice-to-text and responds to user queries in real-time.

---

## 🔄 Execution Flow

1. **User Input:**
   - User types or speaks a query.
   - Voice input is converted using Web Speech API.

2. **Frontend:**
   - JavaScript captures the input.
   - AJAX sends the input to Django backend (`/get_response/`).

3. **Backend (Django View):**
   - Django receives input.
   - Gemini API processes the query and returns a response.

4. **Response Display:**
   - The chatbot's reply is returned to frontend.
   - Chat UI updates the conversation history.

---

## 📦 Tech Stack

- Python (Django)
- Gemini API (LLM)
- HTML, CSS, JavaScript (Frontend)
- SQLite / MySQL (Optional - for storing chat history)
