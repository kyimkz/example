from django.shortcuts import render,HttpResponse
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address
from django.db.models import Count, Avg
from core.forms import ProductReviewForm
from django.http import HttpResponse, JsonResponse

def index(request):
    products = Product.objects.filter(featured=True).order_by("-id") #this part will allow to list products in landing page, also ordered for latest products to be first shown

    context = {
        "products": products
    }

    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.all().order_by("-id") 

    context = {
        "products": products
    }
    
    return render(request, 'core/product-list.html', context)

def aboutus(request):
    
    return render(request, 'core/aboutus.html')

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

def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors" : vendors,
    }
    return render(request, "core/vendor-list.html",context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor = vendor, product_status="published")
    context = {
        "vendor" : vendor,
        "products": products,
    }
    return render(request, "core/vendor-detail.html",context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)

    products = Product.objects.filter(category = product.category).exclude(pid=pid)

    # ------->Getting reviews<-------
    reviews = ProductReview.objects.filter(product = product).order_by("-date")

    # average reviews
    average_review = ProductReview.objects.filter(product = product).aggregate(rating = Avg('rating'))

    #review form
    review_form = ProductReviewForm()
    
    create_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user = request.user,product=product).count()

        if user_review_count > 0:
            create_review = False

    p_image = product.p_images.all() #this line is used to access all the images of ONE PRODUCT

    context = {
        "p": product,
        "create_review": create_review,
        "review_form": review_form,
        "p_image": p_image,
        "average_review": average_review,
        "reviews": reviews,
        "products" : products,
    }

    return render(request, "core/product-detail.html", context)


def add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product = product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )
    context = {
        'user': user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating'],
    }

    average_review = ProductReview.objects.filter(product=product).aggregate(rating = Avg("rating"))
    
    return JsonResponse(
        {
        'bool': True,
        'context': context,
        'average_review' : average_review
        }

    )