from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'accounts/index.html')

def appetizers(request):
    return render(request, 'accounts/appetizers.html')

def breakfast(request):
    return render(request, 'accounts/breakfast.html')

def kaak(request):
    return render(request, 'accounts/kaak.html')

def manakish(request):
    return render(request, 'accounts/manakish.html')

def menu(request):
    return render(request, 'accounts/menu.html')

def pidetr(request):
    return render(request, 'accounts/pidetr.html')

def pizza(request):
    return render(request, 'accounts/pizza.html')

def payment_success(request):
    return render(request, 'accounts/success.html')

def payment_cancel(request):
    return render(request, 'accounts/cancel.html')

def checkout(request):
    """صفحة الدفع"""
    return render(request, "accounts/checkout.html")
