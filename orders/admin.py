# Import Django admin module
from django.contrib import admin

# Import the models to register in admin panel
from orders.models import Order, OrderedItem

# ===========================
# Customize the Order model in the admin panel
# ===========================
class OrderAdmin(admin.ModelAdmin):
    # Add filters on the right sidebar in admin panel
    # Allows you to filter orders by owner or order_status
    list_filter = [
        "owner",
        "order_status",
    ]

    # Add search box in admin panel
    # Allows you to search orders by owner or order id
    search_fields = (
        "owner",  # search by customer name or related user
        "id",     # search by order ID
    )

# Register Order model with custom admin options
admin.site.register(Order, OrderAdmin)

# Note: OrderedItem is not registered here, so it won't appear separately in admin.
# You can register it if you want to manage individual cart items in admin panel.
