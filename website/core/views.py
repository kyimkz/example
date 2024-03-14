from django.shortcuts import render,HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address
from django.db.models import Count, Avg

def index(request):
    products = Product.objects.filter(featured=True).order_by("-id") #this part will allow to list products in landing page, also ordered for latest products to be first shown

    context = {
        "products": products
    }

    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id") 

    context = {
        "products": products
    }

    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category": category,
        "products": products,
    }

    return render(request, 'core/category-product-list.html', context)


def product_detailed_view(request, pid):
    product = Product.objects.get(pid=pid)

    products = Product.objects.filter(category = product.category).exclude(pid=pid)

    # ------->Getting reviews<-------
    reviews = ProductReview.objects.filter(product = product).order_by("-date")

    # average reviews
    average_review = ProductReview.objects.filter(product = product).aggregate(rating = Avg('rating'))


    p_image = product.p_images.all()

    context = {
        "p": product,
        "p_image": p_image,
        "average_review": average_review,
        "reviews": reviews,
        "products" : products,
    }

    return render(request, "core/product-detail.html", context)