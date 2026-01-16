from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_cart(request):
    user = request.user
    customer = user.customer_profile

    try:
        cart = Order.objects.get(owner=customer, order_status=Order.CART_STAGE)
        items = cart.added_item.all()
    except Order.DoesNotExist:
        items = []

    # Calculate subtotal per item
    for item in items:
        item.subtotal = item.quantity * item.product.price

    # Total
    total = sum(item.subtotal for item in items)

    context = {
        'cart': cart if items else None,
        'items': items,
        'total': total
    }
    return render(request, 'cart.html', context)

def remove_item_from_cart(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profile

        # Get the cart safely
        order_obj = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()

        if not order_obj:
            messages.error(request, "No items in cart")
            return redirect('cart')

        # Calculate total
        total = sum(item.quantity * item.product.price for item in order_obj.added_item.all())
        
        # Update order
        order_obj.total_price = total
        order_obj.order_status = Order.ORDER_CONFIRMED
        order_obj.save()

        messages.success(request, "Your order is confirmed!")

    return redirect('cart')


@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity',1))
        product_id=request.POST.get('product_id')
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)

        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity += quantity
            ordered_item.save()

    return redirect('cart')


@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    
    return render(request, 'orders.html',context)
