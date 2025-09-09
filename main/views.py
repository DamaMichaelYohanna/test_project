from django.shortcuts import render, redirect


def index_view(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("The username is", username)
        print("The password is", password)
        return redirect("/")
    else:
        pass

    return render(request, 'login.html')