from django.contrib import admin
from .models import Product

# ----------------------------
# Register Product model in Admin Panel
# ----------------------------

# This makes the Product model visible and manageable
# in the Django Admin interface
admin.site.register(Product)
