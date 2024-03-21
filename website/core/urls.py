from django.urls import path
from core.views import index, product_list_view, category_list_view, details, services, order, returns, career, partnership, payment, category_product_list_view, shipping, product_detail_view, add_review, vendor_list_view, contact, vendor_detail_view, tag_list, aboutus, privacy

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    #Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    path("aboutus/", aboutus, name='aboutus'),
    path("privacy/", privacy, name='privacy'),
    path("contact/", contact, name='contact'),
    path("shipping/", shipping, name='shipping'),
    path("returns/", returns, name='returns'),
    path("payment/", payment, name='payment'),
    path("details/", details, name='details'),
    path("partnership/", partnership, name='partnership'),
    path("career/", career, name='career'),
    path("order/", order, name='order'),
    path("services/", services, name='services'),
    path("add-review/<int:pid>/", add_review, name = "add-review"),

    #Vendor
    path("vendor/", vendor_list_view, name = "vendor-list"),
    path("vendor/<vid>", vendor_detail_view, name = "vendor-detail"),

    #Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
]