from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from cart.models import Cart, CartItem


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key  # Creates session keys if none exists
    if not cart:
        cart = request.session.session_create()
    return cart


# Adding products to cart functionality
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  # cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart')


# Remove from cart functionality
def remove_from_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item > 1:
            cart_item.quantity -= 1  # cart_item.quantity = cart_item.quantity - 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')


# Remove cart item functionality
def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active__in=[True])
        for cart_item in cart_items:
            total += round((cart_item.product.price * cart_item.quantity))
            quantity += cart_item.quantity
        tax = round((2 * total) / 100, 2)
        grand_total = total + tax
    except Cart.DoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, template_name='store/cart.html', context=context)
