from django.contrib import admin

from .models import Order, OrderItems

class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "address", "total", "created_at")
    inlines = [OrderItemInline]

@admin.register(OrderItems)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price", "get_subtotal")

    def get_subtotal(self, obj):
        return obj.get_subtotal()
    get_subtotal.short_description = "Subtotal"
