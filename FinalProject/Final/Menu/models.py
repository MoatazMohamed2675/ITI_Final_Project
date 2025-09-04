from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    @classmethod
    def get_all_menu_items(cls):
        return cls.objects.all()
    
    @classmethod
    def get_menu_item_by_name(cls, name):
        return cls.objects.get(name=name)