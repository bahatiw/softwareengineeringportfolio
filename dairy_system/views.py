from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Farmer, MilkInput, MilkQuality, Order, Inventory, Customer
# Farm Views
def dashboard(request):
    return render(request, 'dairy_system/base.html')

class FarmerListView(ListView):
    model = Farmer
    template_name = 'farmer_list.html'

class FarmerDetailView(DetailView):
    model = Farmer
    template_name = 'farmer_detail.html'

class FarmerCreateView(CreateView):
    model = Farmer
    template_name = 'farmer_form.html'
    fields = ['name', 'contact_info']

class FarmerUpdateView(UpdateView):
    model = Farmer
    template_name = 'farmer_form.html'
    fields = ['name', 'contact_info']

class FarmerDeleteView(DeleteView):
    model = Farmer
    template_name = 'farmer_confirm_delete.html'
    success_url = reverse_lazy('farmer_list')
# Milk input views
class MilkInputListView(ListView):
    model = MilkInput
    template_name = 'milkinput_list.html'

class MilkInputDetailView(DetailView):
    model = MilkInput
    template_name = 'milkinput_detail.html'

class MilkInputCreateView(CreateView):
    model = MilkInput
    template_name = 'milkinput_form.html'
    fields = ['farmer', 'milk_quantity', 'production_date']

class MilkInputUpdateView(UpdateView):
    model = MilkInput
    template_name = 'milkinput_form.html'
    fields = ['farmer', 'milk_quantity', 'production_date']

class MilkInputDeleteView(DeleteView):
    model = MilkInput
    template_name = 'milkinput_confirm_delete.html'
    success_url = reverse_lazy('milkinput_list')
# Milk Quality Views
class MilkQualityListView(ListView):
    model = MilkQuality
    template_name = 'milkquality_list.html'

class MilkQualityDetailView(DetailView):
    model = MilkQuality
    template_name = 'milkquality_detail.html'

class MilkQualityCreateView(CreateView):
    model = MilkQuality
    template_name = 'milkquality_form.html'
    fields = ['farmer', 'fat_content', 'protein_content', 'testing_date', 'quality_inspector']

class MilkQualityUpdateView(UpdateView):
    model = MilkQuality
    template_name = 'milkquality_form.html'
    fields = ['farmer', 'fat_content', 'protein_content', 'testing_date', 'quality_inspector']

class MilkQualityDeleteView(DeleteView):
    model = MilkQuality
    template_name = 'milkquality_confirm_delete.html'
    success_url = reverse_lazy('milkquality_list')
# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'order_quantity', 'status', 'order_date']

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'order_quantity', 'status', 'order_date']

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
# Inventory Views
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'

class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'inventory_form.html'
    fields = ['quantity', 'updated_at']

class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventory_form.html'
    fields = ['quantity', 'updated_at']

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')
