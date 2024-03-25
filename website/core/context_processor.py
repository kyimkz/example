from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    products = Product.objects.all()

    return {
        'categories': categories,
        'vendors': vendors,
        'products': products
    }