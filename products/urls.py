from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    #  specify that the product ID should be an integer, otherwise navigating to products /add will interpret the string add as a product id.
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
