from django.shortcuts import render

from products.models import Product


def home(request):
    products = Product.objects.all().filter(is_available__in=[True])
    context = {
        'products': products,
    }

    return render(request, template_name='index.html', context=context)
