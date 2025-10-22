from django.urls import path
from main.views import index_view, login_view, about_us, contact_us, register_view, create_product, detail_page, user_profile, vendor_profile, logout_view, add_to_cart, cart_view, remove_from_cart

urlpatterns = [
    path('', index_view, name='index'),
    path('detail-page/<int:pk>', detail_page, name='detail_page'),
    path('login/',  login_view, name='login'),
    path('about',  about_us, name='about_us_page'),
    path('contact',  contact_us, name='contact_us_page'),
    path('register',  register_view, name='register'),
    path("add-product", create_product, name='create_product'),
    path("user-profile", user_profile, name='user_profile'),
    path("vendor-profile", vendor_profile, name='vendor_profile'),
    path('logout/', logout_view, name='logout'),
    path('add-to-cart/<int:pk>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name="remove-from-cart"),
    path('cart', cart_view, name='cart_view'),

]


