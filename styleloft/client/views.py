from django.shortcuts import render
from django.http import HttpResponse
from adminDashboard.models import *


# Create your views here.
def home_page(request):
    latest = Product.objects.all().reverse()[:4]
    mostselling = Product.objects.filter(product_category="Top & Tshirt")[:4]
    params = {'latest': latest, 'mostselling': mostselling}
    return render(request, 'home_page.html',params)


def view_by_category(request, category):
    product = Product.objects.filter(product_category=category)
    params = {'products': product, 'category': category}
    return render(request, 'category.html', params)


def view_product_details(request, id):
    product = product = Product.objects.get(id=id)
    params = {'product': product}
    return render(request, 'view_product.html', params)
