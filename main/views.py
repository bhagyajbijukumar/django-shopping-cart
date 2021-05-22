from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def view_product(request, id):
    return HttpResponse(f"test {id}")