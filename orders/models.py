from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    address=models.CharField(max_length=100)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=40)
    zip_code=models.IntegerField()
    
    
    created_at=models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
       return f"#{self.id} by {self.user.username}"
   
   

class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def get_subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product.product_name} (x{self.quantity})"

