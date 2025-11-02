from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from products.models import Product
from .models import CartItems,Cart
from products.models import Product


def cart_create(user):
    try:
        cart=Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user)
    return cart


def add_to_cart(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return ("product does not exist")
    
    cart=cart_create(request.user)
    
    
    try:
        item=CartItems.objects.get(product=product,cart=cart)
        item.quantity +=1
        item.save()
    except CartItems.DoesNotExist:
        item=CartItems(product=product,cart=cart,quantity=1)
        item.save()
        
    return redirect('cart_page')


def cart_delete(request,product_id):
    try:
        item=CartItems.objects.get(id=product_id,cart__user=request.user)
        item.delete()
    except CartItems.DoesNotExist:
        return HttpResponseNotFound("item not exists")
    
    return redirect('cart_page')






def cart_view(request):
    cart=cart_create(request.user)
    items=cart.items.all()
    total=cart.get_total()
    return render(request,'cart_page.html',{"items":items,
                                            "total":total,
                                            "cart":cart,
                                            }) 
    

    
def update_cart(request, item_id):
    try:
        item = CartItems.objects.get(id=item_id, cart__user=request.user)
    except CartItems.DoesNotExist:
        return HttpResponseNotFound("Item not found")

    if request.method == "POST":
        try:
            qty = int(request.POST.get("quantity", 1))  # naya qty form se lo
        except ValueError:
            qty = 1

    if qty > 0:
        item.quantity = qty
        item.save()
    else:
        item.delete()

    return redirect("cart_page")
    
        
        
        
        