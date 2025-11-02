from django.shortcuts import render, redirect
from cart.models import Cart, CartItems
from orders.models import Order, OrderItems   
from django.shortcuts import render, get_object_or_404
from products.models import Product
def checkout(request):
   
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()   
    
    if request.method == "POST":
        address = request.POST.get("address")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        city=request.POST.get("city")
        country=request.POST.get("country")
        zip_code=request.POST.get("zip_code")
        
        order = Order.objects.create(
            user=request.user, 
            address=address,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            city=city,
            country=country,
            zip_code=zip_code,
            total=cart.get_total()
        )

        
        for item in items:
            OrderItems.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            
        cart.items.all().delete()

        
        return redirect("order_detail", order.id)

    
    return render(request, "checkout_page.html", {"cart": cart, "items": items})





def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "order_detail_page.html", {"order": order})
