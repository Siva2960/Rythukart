from django import forms
from .models import Product  # make sure this import is also correct

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'price', 'image','stock']


