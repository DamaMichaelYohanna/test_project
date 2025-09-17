from django.urls import path
from main.views import index_view, login_view, about_us, contact_us, register_view

urlpatterns = [
    path('', index_view, name='index'),
    path('login',  login_view, name='login'),
    path('about',  about_us, name='about_us_page'),
    path('contact',  contact_us, name='contact_us_page'),
    path('register',  register_view, name='register'),

]


