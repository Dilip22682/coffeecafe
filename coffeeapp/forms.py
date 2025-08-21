from django import forms
from coffeeapp.models import coffee_details

class coffeeform(forms.ModelForm):
    class Meta:
        model = coffee_details
        fields = ['coffee_name','coffee_price']