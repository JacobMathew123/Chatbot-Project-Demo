# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # The home page of the blog
    path('register/',views.register,name='register'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
]
