
from django.urls import path
from . import views

urlpatterns=[
    path('',views.coffeeList,name='coffee'),
    path('register/', views.register_user, name='register'),
    # path('base/',views.hello,name='base'),
    path('search/',views.search_coffee_item,name='search_data'), 
    path('order/<int:id>/',views.orderDetails,name='order'),
    path('orders/',views.orders,name='orders'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('add-cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart_view,name='cart'),
    path('remove-cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
 
]
