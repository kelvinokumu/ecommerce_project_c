from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form":form})