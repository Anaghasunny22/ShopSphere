from django.db import models

# ----------------------------
# Product Model
# ----------------------------
class Product(models.Model):

    # Constants for delete status
    LIVE = 1
    DELETE = 0

    # Choices shown in Django Admin
    DELETE_CHOICE = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )

    # Product title/name
    title = models.CharField(max_length=200)

    # Product price
    price = models.FloatField()

    # Detailed product description
    description = models.TextField()

    # Product image (stored inside media/ folder)
    image = models.ImageField(upload_to='media/')

    # Priority for sorting products (higher = more important)
    priority = models.IntegerField(default=0)

    # Soft delete status (Live or Deleted)
    delete_status = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)

    # Automatically stores date when product is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updates date when product is modified
    updated_at = models.DateTimeField(auto_now=True)

    # String representation (shows product title in admin panel)
    def __str__(self):
        return self.title
