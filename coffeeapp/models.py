from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class coffee_details(models.Model):
    coffee_name=models.CharField(max_length=100)
    coffee_price=models.FloatField()
    coffee_description=models.TextField(blank=True)
    coffee_img=models.ImageField(upload_to='coffeeImages',blank=True,null=True)
    def __str__(self):
        return self.coffee_name
    
class chai_details(models.Model):
    chai_name=models.CharField(max_length=100)
    chai_price=models.FloatField()
    chai_description=models.TextField(blank=True)
    chai_img=models.ImageField(upload_to='chaii_img',blank=True,null=True)
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    coffee = models.ForeignKey(coffee_details,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.coffee.coffee_price
    

class Order(models.Model):
    PAYMENT_CHOICES = (
        ('COD','Cash On Delivery'),
        ('UPI','UPI'),
        ('CARD','Debit/Credit Card'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20,choices=PAYMENT_CHOICES)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

 

# class Order(models.Model): 

#     user = models.ForeignKey(User,on_delete=models.CASCADE)

#     total_price= models.IntegerField()

#     razorpay_order_id = models.CharField(max_length=100)

#     razorpay_payment_id = models.CharField(max_length=100,null=True,blank=True)

#     paid = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    coffee = models.ForeignKey(coffee_details,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def total_price(self):
        return self.quantity * self.price
    