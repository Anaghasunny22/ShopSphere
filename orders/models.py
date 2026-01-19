# Import Django models
from django.db import models

# Import related models
from customers.models import Customer  # Customer model for linking orders
from products.models import Product    # Product model for items in the order

# ===========================
# Order Model
# ===========================
class Order(models.Model):
    # Constants for delete status
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = (
        (LIVE, 'Live'),    # Active order
        (DELETE, 'Delete') # Deleted/inactive order
    )

    # ===========================
    # Order Status Constants
    # ===========================
    CART_STAGE = 0        # Items are in cart but not confirmed
    ORDER_CONFIRMED = 1   # Order has been confirmed
    ORDER_PROCESSED = 2   # Order is being processed
    ORDER_DELIVERED = 3   # Order delivered to customer
    ORDER_REJECTED = 4    # Order rejected/cancelled

    STATUS_CHOICE = (
        (CART_STAGE, 'CART_STAGE'),
        (ORDER_CONFIRMED, 'ORDER_CONFIRMED'),
        (ORDER_PROCESSED, 'ORDER_PROCESSED'),
        (ORDER_DELIVERED, 'ORDER_DELIVERED'),
        (ORDER_REJECTED, 'ORDER_REJECTED'),
    )

    # Field to store current status of the order
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)

    # Link order to a Customer
    # on_delete=models.SET_NULL → If customer is deleted, keep the order but set owner to null
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')

    # Total price of all items in the order
    total_price = models.FloatField(default=0)

    # Delete status of order (Live or Delete)
    delete_status = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)

    # Automatically store when order is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically update when order is updated
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the Order
    def __str__(self):
        return f"Order-{self.id}-{self.owner.name}"  # Example: Order-1-John

# ===========================
# OrderedItem Model
# ===========================
class OrderedItem(models.Model):
    # Link to Product
    # on_delete=models.SET_NULL → If product is deleted, keep the OrderedItem but set product to null
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='added_carts')

    # Quantity of product in the cart/order
    quantity = models.IntegerField(default=1)

    # Link to Order (owner)
    # on_delete=models.CASCADE → If order is deleted, delete all OrderedItems related to it
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_item')
