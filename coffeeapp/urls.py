
from django.urls import path
from . import views

urlpatterns=[
    path('',views.coffeeList,name='coffee'),
    path('base/',views.hello,name='base'),
    path('search/',views.search_coffee_item,name='search_data'), 
    path('order/<int:id>/',views.orderDetails,name='order'),
    
 
]
