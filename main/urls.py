from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("chatbot/chat/", views.chat_with_ai, name="chat_with_ai"),
    path("chatbot/download-audio", views.download_audio, name="download_audio"),
]