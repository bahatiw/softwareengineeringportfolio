# forms
from django import forms
from .models import Farmer, MilkInput, Order, Inventory

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'contact_info']

class MilkInputForm(forms.ModelForm):
    class Meta:
        model = MilkInput
        fields = ['farmer', 'milk_quantity', 'production_date']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'order_quantity', 'status', 'order_date']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name','quantity']
