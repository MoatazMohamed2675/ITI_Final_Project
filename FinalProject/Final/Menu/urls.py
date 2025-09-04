from django.urls import path
from .views import *
from django.urls import include
from Orders.views import *

urlpatterns = [ 
  path('', menu_list, name='menu_list'),
  path('add/', add_item, name='add_item'),
  path('delete/<int:item_id>/', delete_item, name='delete_item'),
  path('update/<int:item_id>/', update_item, name='update_item'),
  path('search/', search_Menu, name='search_menu'),
  path('orders/', include('Orders.urls')),
  path('customers/', include('Customers.urls'))
]