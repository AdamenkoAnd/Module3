from django.urls import path
from shop.views import index, about, contact,product_list, product_detail, login_view, register_view, logout_view

urlpatterns = [
    path('', index, name='index_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page'),
    path('products', product_list, name='product_list_page'),
    path('products/<int:pk>', product_detail, name='product_detail_page'),
    path('login', login_view, name='login_view_page'),
    path('register',register_view, name='register_view_page'),
    path('logout', logout_view, name='logout_view_page')
]