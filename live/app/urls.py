
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
    path("signin",views.signin),
    path("verifyotp",views.verifyotp),
    path("terms",views.terms),
    path("plans",views.plans),
    path("plans1",views.plans1),
    path("doctor",views.doctor),
    path("doctorprofile",views.doctorprofile),
    path("doctorlogin",views.doctorlogin),
      path("doctorsignin",views.doctorsignin),
      path("doctor_login",views.doctor_login),
      path("docregister",views.docregister),
    
]