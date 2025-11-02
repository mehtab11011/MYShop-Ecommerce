from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"Cart of {self.user.username}")
    
    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.total()
        return total
   
    

class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return (f"{self.product.product_name} (x{self.quantity})")
    
    def total(self):
        return self.product.price * self.quantity
    


# Create your models here.
