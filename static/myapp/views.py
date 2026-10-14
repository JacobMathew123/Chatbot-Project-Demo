from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'pages/login.html')
def register(request):
    return render(request,'pages/register.html')
def chatbot(request):
    return render(request,'pages/chatbot.html')
def home(request):
    return render(request,'pages/home.html')
def about(request):
    return render(request,'pages/about.html')