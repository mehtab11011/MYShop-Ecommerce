from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from products.models import Product
from django.core.paginator import Paginator

def home_page(request):
    electronics=Product.objects.filter(category='electronics').first()
    fashion=Product.objects.filter(category='fashion').first()
    home=Product.objects.filter(category='home').first()
    data={
        'electronics':electronics,
        'fashion':fashion,
        'home':home,
        
    }
    
    
    return render(request,'home_page.html/',data)




def product_page(request):
    data = Product.objects.all()
    st = request.GET.get("q")

    if st:  
        data = data.filter(Q(product_name__icontains=st) |
                           Q(category__icontains=st))

    
    paginator = Paginator(data, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products_page.html",
        {"page_obj": page_obj, "st": st}
    )

    

def detail_page_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail_page.html', {"product": product})
