
from django.contrib import admin
from django.urls import path,include
from .views import signup_view,login_view,logout_view
urlpatterns = [
   path("signup",signup_view,name="signup_page"),
   path("login",login_view,name="login_page"),
   path("logout/",logout_view, name="logout"),
   
    
]


