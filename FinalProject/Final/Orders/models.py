from django.db import models
from django.db.models import Sum
from Menu.models import Menu
from Customers.models import Customer
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)  
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    def save(self, *args, **kwargs):
        # create or get customer when saving
        customer, created = Customer.objects.get_or_create(
            name=self.customer_name,
            phone=self.phone,
            defaults={"email": self.email}
        )
        self.customer = customer
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        result = self.orderitem_set.aggregate(Sum("total_price"))['total_price__sum']
        return result or 0
    
    @classmethod
    def get_orders(cls):
        return cls.objects.all()
    
    @classmethod
    def get_order_by_id(cls, order_id):
        return cls.objects.get(id=order_id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)



    @classmethod
    def get_order_items(cls):
        return cls.objects.all()
    
    @classmethod
    def get_order_item_by_id(cls, order_item_id):
        return cls.objects.get(id=order_item_id)
