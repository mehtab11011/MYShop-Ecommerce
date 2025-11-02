from django.db import models

class Product(models.Model):
    # Choices for Category
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('home', 'Home & Living'),
        ('sports', 'Sports'),
    ]

    # Choices for Status
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    product_name = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='electronics'
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    image = models.FileField(upload_to="products/")
    detail = models.TextField(default="Not available")


    def __str__(self):
        return self.product_name
    
