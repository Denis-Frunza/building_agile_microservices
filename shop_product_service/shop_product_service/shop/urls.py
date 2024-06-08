from django.urls import path
from shop import views

urlpatterns = [
    path(f'{views.CategoryList.name}', views.CategoryList.as_view(), name=views.CategoryList.name), # Category
    path(f'{views.CategoryDetail.name}/<int:pk>', views.CategoryDetail.as_view(), name=views.CategoryDetail.name), # Category detail

    path(f'{views.ProductList.name}', views.ProductList.as_view(), name=views.ProductList.name), # Product
    path(f'{views.ProductDetail.name}/<int:pk>', views.ProductDetail.as_view(), name=views.ProductDetail.name), # Product detail

    path(f'{views.ProductImageList.name}', views.ProductImageList.as_view(), name=views.ProductImageList.name), # Product-image
    path(f'{views.ProductImageDetail.name}/<int:pk>', views.ProductImageDetail.as_view(), name=views.ProductImageDetail.name), # Product-image detail

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
