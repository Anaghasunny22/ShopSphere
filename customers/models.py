# Import Django's model system
from django.db import models

# Import User model to link our Customer to Django's authentication system
from django.contrib.auth.models import User

# ===========================
# Customer Model
# ===========================
class Customer(models.Model):
    # Constants to represent delete status
    LIVE = 1
    DELETE = 0

    # Choices tuple for delete_status field (for dropdowns in admin or forms)
    DELETE_CHOICE = (
        (LIVE, 'Live'),     # 1 represents active/live customer
        (DELETE, 'Delete')  # 0 represents deleted/inactive customer
    )

    # Customer's full name
    name = models.CharField(max_length=200)  # max 200 characters

    # Customer's address
    address = models.TextField()  # TextField allows long text

    # Link to Django User (One-to-One relationship)
    # If the user is deleted, delete the related customer (on_delete=models.CASCADE)
    # related_name allows reverse lookup like user.customer_profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')

    # Customer's phone number
    phone = models.CharField(max_length=10)  # max 10 characters, suitable for phone numbers

    # Priority field (optional usage, default is 0)
    priority = models.IntegerField(default=0)

    # Delete status: Live or Delete, default is Live
    delete_status = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)

    # Auto set creation date when new Customer is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Auto update date whenever Customer record is updated
    updated_at = models.DateTimeField(auto_now=True)

    # ===========================
    # String representation of the model
    # ===========================
    # This is useful in admin panel and debugging
    def __str__(self):
        return self.user.username  # Display the linked username when printing the object
