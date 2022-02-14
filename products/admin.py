from django.contrib import admin
from products.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available')


admin.site.register(Product, ProductAdmin)
