from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from products.models import Product
from category.models import Category
from subcategory.models import Subcategory


# Create your views here.


def store(request, category_slug=None, subcategory_slug=None):
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available__in=[True])
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

        if subcategory_slug is not None:
            subcategories = get_object_or_404(Subcategory, slug=subcategory_slug)
            products = Product.objects.filter(subcategory=subcategories, is_available__in=[True])
            product_count = products.count()

    else:
        products = Product.objects.all()
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, template_name='store/store.html', context=context)


# Product detail functionality
def product_detail(request, category_slug=None, subcategory_slug=None, product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug, subcategory__slug=subcategory_slug,
                                             slug=product_slug)

    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, template_name='store/product_detail.html', context=context)


# Search functionality
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__contains=keyword) | Q(product_name__contains=keyword))
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, template_name='store/store.html', context=context)
