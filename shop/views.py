from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
    "user_id": 12345,
    "username": "example_user",
    "theme": "dark"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    return render(request, 'products.html')

def product_detail(request, pk):
    return render(request, 'product_detail.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def logout_view(request):
    return HttpResponse('выход пользователя')