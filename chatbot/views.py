from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from decouple import config

# ✅ Load Gemini API Key from .env
genai.configure(api_key=config("GEMINI_API_KEY"))

def index(request):
    """Render the chatbot page."""
    return render(request, 'index.html')

def get_response(request):
    """Handle POST requests and return Gemini AI responses."""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        ai_response = "No response from Gemini AI"
        
        if user_input:
            try:
                # ✅ Use correct API format with the latest version
                model = genai.GenerativeModel(model_name="gemini-1.5-pro")
                response = model.generate_content([user_input])  # Get the AI response
                ai_response = response.text if response.text else "No response from Gemini AI"
                
            except Exception as e:
                ai_response = f"Error: {str(e)}"
        else:
            ai_response = "Please enter a message."

        return JsonResponse({"response": ai_response})

    return JsonResponse({"error": "Invalid request"})
