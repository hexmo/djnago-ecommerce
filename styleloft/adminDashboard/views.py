from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login/')
def add_product(request):
    if request.method == 'POST' and request.FILES['product_photo']:
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_category = request.POST['product_category']
        product_size = request.POST['product_size']
        product_brand = request.POST['product_brand']
        product_material = request.POST['product_material']
        product_color = request.POST['product_color']
        # creating and saving object
        product_object = Product.objects.create(product_name=product_name, product_price=product_price, product_size=product_size, product_category=product_category,
                                                product_brand=product_brand, product_material=product_material, product_color=product_color, product_photo=request.FILES['product_photo'])
        product_object.save()

        return render(request, 'add_product.html')
    else:
        return render(request, 'add_product.html')

@login_required(login_url='/login/')
def manage_product(request):
    product = Product.objects.all()
    params = {'products': product}
    return render(request, 'manage_product.html', params)

@login_required(login_url='/login/')
def edit_product(request, id):
    if request.method == 'POST':
        product = product = Product.objects.get(id=id)

        product.product_name = request.POST['product_name']
        product.product_price = request.POST['product_price']
        product.product_category = request.POST['product_category']
        product.product_size = request.POST['product_size']
        product.product_brand = request.POST['product_brand']
        product.product_material = request.POST['product_material']
        product.product_color = request.POST['product_color']

        # image file management
        if 'product_photo' in request.FILES:
            product.product_photo = request.FILES['product_photo']
        # saving object
        product.save()
        return redirect('/dashboard/manageproduct')
    else:
        product = product = Product.objects.get(id=id)
        params = {'product': product}
        return render(request, 'edit_product.html', params)

@login_required(login_url='/login/')
def delete_product(request, id):
    product = product = Product.objects.get(id=id)
    product.delete()
    return redirect('/dashboard/manageproduct') 
