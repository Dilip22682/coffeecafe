from django.contrib import admin
from coffeeapp.models import coffee_details,chai_details,Cart, Order, OrderItem

# Register your models here.
# admin.site.register(coffee_details)
@admin.register(chai_details)
class chai_detailsAdmin(admin.ModelAdmin):
    list_display=['chai_name','chai_price','chai_description','chai_img']

@admin.register(coffee_details)
class coffee_detailsAdmin(admin.ModelAdmin):
    list_display=['coffee_name','coffee_price','coffee_description','coffee_img']
    
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'coffee', 'quantity')
    list_filter = ('user',)
    search_fields = ('user__username', 'coffee__name')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_method', 'total_amount', 'created_at')
    list_filter = ('payment_method', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'coffee', 'quantity', 'price')

