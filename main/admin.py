from django.contrib import admin

from .models import Product, Message, Profile, Cart

admin.site.register(Product)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Cart)
