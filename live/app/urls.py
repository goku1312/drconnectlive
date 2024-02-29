
from django.urls import path
from app import views

urlpatterns = [
   
    path('',views.index),
    path('index',views.index),
    path('cart',views.cart),
    path('checkout',views.checkout),
    path("shop",views.shop),
    path("blog",views.blog),
    path("blogdetails",views.blogdetails),
    path("vendor",views.vendor),
    path("contact",views.contact),
    path("vendorprofile",views.vendorprofile),
    path("compare",views.compare),
    path("login",views.login),
    path("vendordashboard",views.vendordashboard),
    path("register",views.register),
    path("user_login",views.user_login),
    path("logout",views.logout),
    path("new_page",views.new_page),
    path("otp",views.otp),
    # path("resent",views.resent),
    path("newlogin",views.newlogin),
]