from django.contrib import admin
from django.urls import path,include
from api import views
from .views import Index ,order
urlpatterns = [
    path("",Index.as_view(),name='index'),
    path("signup", views.signup,name='signup'),
    path("login",views.logins,name='login'),
    path("cart", views.cart,name='cart'),
    path("logout", views.logout,name='logout'),
    path("checkout", views.checkout,name='checkout'),
    path("order", order.as_view(),name='order')
]
