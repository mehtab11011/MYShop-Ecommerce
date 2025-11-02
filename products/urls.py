from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include
from .views import home_page,product_page,detail_page_view

urlpatterns = [
    path("",home_page,name="home_page"),
    path("product_page/",product_page,name="product_page"),
    path("product_detail/<int:id>/",detail_page_view,name="product_detail"),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)