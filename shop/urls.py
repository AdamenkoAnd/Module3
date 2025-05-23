from django.urls import path
from shop.views import index, about, contact,product_list, product_detail, login_view, register_view, logout_view

urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact),
    path('products', product_list),
    path('products/<int:pk>', product_detail),
    path('login', login_view),
    path('register',register_view),
    path('logout', logout_view)
]