
from django.urls import path
from coffeeapp import views

urlpatterns=[
    # path('',views.hello,name='base'),
    path('',views.coffeeList,name='coffee'),
    path('search',views.searchdata,name='searchdata'),
    path('order/<int:id>/',views.orderDetails,name='order'),
]
