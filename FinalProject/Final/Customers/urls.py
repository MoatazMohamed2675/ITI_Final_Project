from django.urls import path
from .views import *



urlpatterns = [ 
    path('', customers_list, name='customers_list'),
    path('add/', add_customer, name='add_customer'),
    path('update/<int:customer_id>/', update_customer, name='update_customer'),
    path('delete/<int:customer_id>/', delete_customer, name='delete_customer'),
]