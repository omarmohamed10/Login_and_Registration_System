from django.shortcuts import render, redirect
from .models import Product
from django.forms import modelform_factory


# Create your views here.

def details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/details.html', {'product': product})


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})


product_Form = modelform_factory(Product, exclude=[])


def add(request):
    if request.method == "POST":
        form = product_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')

    else:
        form = product_Form()
    context = {'form': form}
    return render(request, 'products/add_product.html', context)
