from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/subcategory<slug:subcategory_slug>/', views.store, name='products_by_subcategory'),
    path('category/<slug:category_slug>/subcategory/<slug:subcategory_slug>/<slug:product_slug>/ ', views.product_detail,
         name='product_detail'),
    path('search/', views.search, name='search'),
]
