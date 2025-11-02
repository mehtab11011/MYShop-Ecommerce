from django.contrib import admin
from .models import Cart,CartItems

class CartItemsInline(admin.TabularInline):
    model=CartItems
    extra=0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user',"created_at","get_total"]
    inlines=[CartItemsInline]
   
       
@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display=["cart","product","quantity","total"]
    search_fields=("cart","product")

