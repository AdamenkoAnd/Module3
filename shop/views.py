from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('главная страница магазина')

def about(request):
    return HttpResponse('информация о компании')

def contact(request):
    return HttpResponse('форма или контакты')

def product_list(request):
    return HttpResponse('список товаров')

def product_detail(request, pk):
    return HttpResponse('подробности о конкретном товаре')

def login_view(request):
    return HttpResponse('форма входа')

def register_view(request):
    return HttpResponse('форма регистрации')

def logout_view(request):
    return HttpResponse('выход пользователя')