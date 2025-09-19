from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Product

def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products}) 


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


# views here are for products
def create_product(request):
    """function to upload a new product"""
    if request.method == "POST":
        product_name = request.POST['name']
        product_description = request.POST['description']
        product_price = request.POST['price']
        product_image = request.FILES['image']
        new_product = Product(
            name=product_name,
            description=product_description,
            price=product_price,
            image=product_image
        )
        new_product.save()
        print(product_name, product_description, product_price, product_image)

        return redirect('/')

    return render(request, 'add_product.html')