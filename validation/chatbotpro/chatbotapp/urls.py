from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('register/',views.register_view,name='register_view'),
    path('log/',views.login_view,name='login_view'),
    path('chatbot/',views.chatbot,name='chatbot'),
]