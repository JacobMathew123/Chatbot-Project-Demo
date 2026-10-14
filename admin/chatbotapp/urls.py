from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('chatbot/',views.chatbot,name='chatbot'),
]