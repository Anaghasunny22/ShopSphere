# Import path function to define URLs
from django.urls import path

# Import all view functions from this app
from . import views

# ===========================
# URL Patterns for Cart & Orders
# ===========================
urlpatterns = [
    # URL for showing the cart page
    # Example: /cart/
    # Calls the show_cart view function
    path('cart/', views.show_cart, name='cart'),

    # URL for showing all past orders of the customer
    # Example: /orders/
    # Calls the show_orders view function
    path('orders/', views.show_orders, name='orders'),

    # URL for adding an item to the cart
    # Typically called via POST when a user clicks "Add to Cart"
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),

    # URL for removing a specific item from the cart
    # <int:pk> captures the primary key of the OrderedItem to remove
    # Example: /remove_item/5 → removes OrderedItem with id=5
    path('remove_item/<int:pk>', views.remove_item_from_cart, name='remove_item'),

    # URL to checkout the cart and confirm the order
    # Example: /checkout_cart/
    path('checkout_cart/', views.checkout_cart, name='checkout')
]
