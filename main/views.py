from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username_value = request.POST['username']
        password_value = request.POST['password']
        user = authenticate(request,
                             username=username_value, 
                             password=password_value)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
  
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = 'Test First Name'
        user.last_name = 'Test Last Name'
        user.save()
        return redirect('/login')
    return render(request, 'register.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')