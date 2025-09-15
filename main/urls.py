from django.urls import path
from main.views import index_view, login, about_us, contact_us

urlpatterns = [
    path('', index_view, name='index'),
    path('login',  login, name='login_page'),
    path('about',  about_us, name='about_us_page'),
    path('contact',  contact_us, name='contact_us_page')

]


