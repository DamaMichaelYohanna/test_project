from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product, Message, Profile
from django.contrib.auth.decorators import login_required

def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def detail_page(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'detail_page.html', {'product': product}) 


def login_view(request):
    if request.method == 'POST':
        username_value = request.POST['username']
        password_value = request.POST['password']
        user = authenticate(request,
                             username=username_value, 
                             password=password_value)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect("/")
        else:
            messages.error(request, 'Login failed. Please try again.')
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
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = 'Test First Name'
            user.last_name = 'Test Last Name'
            user.save()
            profile = Profile.objects.create(user=user, is_vendor=False)
            profile.phone_no = request.POST.get('phone_no', '09876543210')
            profile.address = request.POST.get('address', 'Default Address')
            profile.image = request.FILES.get('image', 'default.jpg') 
            profile.save
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('/login')
        except:
            return render(request, 'register.html', {'error': 'Username already exists'})
    return render(request, 'register.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        message = Message.objects.create(name=name, email=email, message=message)
        message.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/')
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

@login_required
def user_profile(request):
    user_detail = User.objects.get(username=request.user.username)
    user_profile = user_detail.profile
    return render(request, 'user_profile.html', 
                  {'user_detail': user_detail,
                   "user_profile": user_profile})

def vendor_profile(request):
    user_detail = User.objects.get(username=request.user.username)
    if user_detail.profile.is_vendor:
        pass
    else:
        return redirect('user_profile')
    user_profile = user_detail.profile
    return render(request, 'user_profile.html', 
                  {'user_detail': user_detail,
                   "user_profile": user_profile})
    return render(request, 'vendor_profile.html')