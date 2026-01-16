from django.db import models
from customers.models import Customer
from products.models import Product

# model for Order.

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))

    
    # Order Status.
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE = (
        (CART_STAGE, 'CART_STAGE'),
        (ORDER_CONFIRMED,'ORDER_CONFIRMED'),
        (ORDER_PROCESSED,'ORDER_PROCESSED'),
        (ORDER_DELIVERED,'ORDER_DELIVERED'),
        (ORDER_REJECTED,'ORDER_REJECTED')
)

    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True,related_name='orders')
    total_price = models.FloatField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Order-{self.id}-{self.owner.name}"


class OrderedItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_item')

   

