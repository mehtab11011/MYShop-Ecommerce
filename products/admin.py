from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "price", "stock", "category", "status",'detail')
    list_filter = ("category", "status")
    search_fields = ("product_name", "category")
    list_editable = ("price", "stock", "status")   
    ordering = ("-id",)  


