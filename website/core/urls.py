from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, product_detail_view, add_review, vendor_list_view, vendor_detail_view, tag_list, aboutus

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    #Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    path("aboutus/", aboutus, name='aboutus'),
    path("add-review/<int:pid>/", add_review, name = "add-review"),

    #Vendor
    path("vendor/", vendor_list_view, name = "vendor-list"),
    path("vendor/<vid>", vendor_detail_view, name = "vendor-detail"),

    #Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
]