from django.urls import path
from .views import *
from django.urls import include

urlpatterns = [ 
    path('',order_list, name='order_list'),
    path('add/', add_order, name='add_order'),
    path('delete/<int:order_id>/', delete_order, name='delete_order'),
    path('update/<int:order_id>/', update_order, name='update_order')
]