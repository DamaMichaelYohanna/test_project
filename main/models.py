from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"
    

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100,)
    image = models.ImageField()
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    """Database table for adding items to cart"""
    customer = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}'s cart"