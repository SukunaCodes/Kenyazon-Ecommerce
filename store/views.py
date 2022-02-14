from django.shortcuts import render, get_object_or_404
from products.models import Product
from category.models import Category
from subcategory.models import Subcategory


# Create your views here.


def store(request, category_slug=None, subcategory_slug=None):

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available__in=[True])
        product_count = products.count()

        if subcategory_slug is not None:
            subcategories = get_object_or_404(Subcategory, slug=subcategory_slug)
            products = Product.objects.filter(subcategory=subcategories, is_available__in=[True])
            product_count = products.count()

    else:
        products = Product.objects.all()
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, template_name='store/store.html', context=context)
