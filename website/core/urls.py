from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, add_review

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),

    #add review
    path("add-review/<int:pid>/", add_review, name = "add-review"),
]