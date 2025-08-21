from django.db import models

# Create your models here.

class coffee_details(models.Model):
    coffee_name=models.CharField(max_length=100)
    coffee_price=models.FloatField()
    coffee_description=models.TextField(blank=True)
    coffee_img=models.ImageField(upload_to='coffeeImages',blank=True,null=True)
    
class chai_details(models.Model):
    chai_name=models.CharField(max_length=100)
    chai_price=models.FloatField()
    chai_description=models.TextField(blank=True)
    chai_img=models.ImageField(upload_to='chaii_img',blank=True,null=True)
    
class order_details(models.Model):
    units=models.IntegerField()
    
    
    
    