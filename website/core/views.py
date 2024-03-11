from django.shortcuts import render,HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address

def index(request):
    product = Product.objects.all()#this part will allow to list products in landing page(might change later on)

    context = {
        "products": product
    }

    return render(request, 'core/index.html')
