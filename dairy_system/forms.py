# forms
from django import forms
from .models import Farmer, MilkInput, MilkQuality, Order, Inventory

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'contact_info']

class MilkInputForm(forms.ModelForm):
    class Meta:
        model = MilkInput
        fields = ['farmer', 'milk_quantity', 'production_date']

class MilkQualityForm(forms.ModelForm):
    class Meta:
        model = MilkQuality
        fields = ['farmer', 'fat_content', 'protein_content', 'testing_date', 'quality_inspector']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'order_quantity', 'status', 'order_date']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['quantity', 'updated_at']
