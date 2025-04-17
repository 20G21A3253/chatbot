from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link chat to a specific user
    user_message = models.TextField()  # Store the message from the user
    bot_response = models.TextField()  # Store the response from the bot
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically store the timestamp of the chat

    def __str__(self):
        return f"Chat by {self.user.username} at {self.timestamp}"

