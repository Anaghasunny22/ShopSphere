# Import necessary Django modules
from django.shortcuts import render, redirect  # render: to display templates, redirect: to redirect users
from .models import Order, OrderedItem       # Import Order and OrderedItem models from this app
from django.contrib import messages          # To show success or error messages
from products.models import Product          # Import Product model to link items in cart
from django.contrib.auth.decorators import login_required  # To restrict certain views to logged-in users

# ===========================
# View: Display Cart
# ===========================
def show_cart(request):
    user = request.user  # Get currently logged-in user
    customer = user.customer_profile  # Get the related Customer profile

    try:
        # Try to get the current active cart for this customer
        cart = Order.objects.get(owner=customer, order_status=Order.CART_STAGE)
        items = cart.added_item.all()  # Get all items added to the cart
    except Order.DoesNotExist:
        # If no cart exists, set items to empty list
        items = []

    # Calculate subtotal for each item in cart
    for item in items:
        item.subtotal = item.quantity * item.product.price  # Quantity * product price

    # Calculate total price of the cart
    total = sum(item.subtotal for item in items)

    # Pass cart, items, and total to the template
    context = {
        'cart': cart if items else None,
        'items': items,
        'total': total
    }
    return render(request, 'cart.html', context)  # Render cart.html template with context

# ===========================
# View: Remove item from cart
# ===========================
def remove_item_from_cart(request, pk):
    item = OrderedItem.objects.get(pk=pk)  # Get the OrderedItem by primary key
    if item:
        item.delete()  # Delete the item from cart
    return redirect('cart')  # Redirect back to cart page

# ===========================
# View: Checkout Cart
# ===========================
def checkout_cart(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profile

        # Get the current cart (if exists) safely
        order_obj = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()

        if not order_obj:
            # Show error if no items in cart
            messages.error(request, "No items in cart")
            return redirect('cart')

        # Calculate total price
        total = sum(item.quantity * item.product.price for item in order_obj.added_item.all())
        
        # Update the order object
        order_obj.total_price = total
        order_obj.order_status = Order.ORDER_CONFIRMED  # Mark as confirmed order
        order_obj.save()  # Save changes

        # Show success message
        messages.success(request, "Your order is confirmed!")

    return redirect('cart')  # Redirect to cart page after checkout

# ===========================
# View: Add item to cart
# ===========================
@login_required(login_url='account')  # Ensure user is logged in to add items
def add_to_cart(request):
    if request.POST:  # Only handle POST requests
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity', 1))  # Default quantity is 1
        product_id = request.POST.get('product_id')  # Get product id from form

        # Get or create a cart for this customer
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        # Get the product to add
        product = Product.objects.get(pk=product_id)

        # Get or create OrderedItem for this product in the cart
        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )

        if created:
            # If new item, set quantity
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            # If already exists, increment quantity
            ordered_item.quantity += quantity
            ordered_item.save()

    return redirect('cart')  # Redirect back to cart page

# ===========================
# View: Show all previous orders
# ===========================
@login_required(login_url='account')  # User must be logged in
def show_orders(request):
    user = request.user
    customer = user.customer_profile

    # Get all orders except the current cart
    all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)

    context = {'orders': all_orders}

    return render(request, 'orders.html', context)  # Render orders.html template with context
