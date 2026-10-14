from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chatbot(request):
    return render(request, 'chatbot.html')

# register validation
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use 'username' instead of 'name'
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
    
        if not username or not email or not password:
            messages.error(request, 'All fields are required')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! Please login!')
            return redirect('login_view')
    return render(request, 'register.html')

# login validation
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatbot')  # Redirect to the home page (or wherever you want)
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')  # Re-render the login page with error message
    return render(request, 'login.html')  # Render the login page for GET requests


# logout validation
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login_view') 
