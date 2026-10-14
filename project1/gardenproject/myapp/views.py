from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout


# Create your views here.

def chatbot(request):
    return render(request,'pages/chatbot.html')
def home(request):
    return render(request,'pages/home.html')
def about(request):
    return render(request,'pages/about.html')

# register validation

def register(request):
    if request.method =='POST':
       username=request.POST.get('username','')
       email=request.POST.get('email','')
       password=request.POST.get('password','')
       confirm_password=request.POST.get('confirm_password','')

       if not username or not email or not password:
          messages.error(request,'All fields are required')
    #    elif password != (r'/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/',password):
    #        messages.error(request,'Please enter a valid password.It must be at least 8 characters long and include at least one letter and one number')
       elif password != confirm_password:
          messages.error(request,'Password do not match')
       elif User.objects.filter(username=username).exists():
          messages.error(request,'Username already exists')
       elif User.objects.filter(email=email).exists():
          messages.error(request,'Email already exists')
       else:
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save()
          messages.success(request,'Account created successfuly! Please login!')
          return redirect('login_view')
    return render(request,'pages/register.html')


# login validation

def login_view(request):
    if request.method =='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        User=authenticate(request,username=username,password=password)
        if User is not None:
            login(request,User)
            return redirect('chatbot')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'pages/login.html')


# logout validation

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfuly!')
    return redirect('login_view')