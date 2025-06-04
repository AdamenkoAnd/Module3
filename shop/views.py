from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "welcome_message": "Добро пожаловать в PhoneShop!",
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        "company_name": "PhoneShop",
        "year_founded": 2025,
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        "email": "Phohe@gmail.com",
        "phone": "+420 000 000 000",
    }
    return render(request, 'contact.html', context)

def product_list(request):
    context = {
    "phones": 'phones',
    }
    return render(request, 'products.html', context)

def product_detail(request, pk):
    return render(request, 'product_detail.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def logout_view(request):
    return HttpResponse('выход пользователя')