from django.contrib import admin
from coffeeapp.models import coffee_details,chai_details

# Register your models here.
# admin.site.register(coffee_details)
@admin.register(chai_details)
class chai_detailsAdmin(admin.ModelAdmin):
    list_display=['chai_name','chai_price','chai_description','chai_img']

@admin.register(coffee_details)
class coffee_detailsAdmin(admin.ModelAdmin):
    list_display=['coffee_name','coffee_price','coffee_description','coffee_img']
