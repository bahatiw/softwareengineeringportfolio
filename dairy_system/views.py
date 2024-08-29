from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Farmer, MilkInput, Order, Inventory, Customer, Product
# Farm Views
def dashboard(request):
    return render(request, 'dairy_system/base.html')

class FarmerListView(ListView):
    model = Farmer
    template_name = 'farmer_list.html'
    context_object_name = 'farmers'
    # success_url = reverse_lazy('farmer_list') 

class FarmerDetailView(DetailView):
    model = Farmer
    template_name = 'farmer_detail.html'
    success_url = reverse_lazy('farmer_list') 

class FarmerCreateView(CreateView):
    model = Farmer
    template_name = 'farmer_form.html'
    fields = ['first_name', 'second_name', 'id_number']  # Updated to use the new fields
    success_url = reverse_lazy('farmer_list') 

class FarmerUpdateView(UpdateView):
    model = Farmer
    template_name = 'farmer_form.html'
    fields = ['first_name', 'second_name', 'id_number']  # Updated to use the new fields
    success_url = reverse_lazy('farmer_list') 

class FarmerDeleteView(DeleteView):
    model = Farmer
    template_name = 'farmer_confirm_delete.html'
    success_url = reverse_lazy('farmer_list')
# Milk input views
class MilkInputListView(ListView):
    model = MilkInput
    template_name = 'milkinput_list.html'
    success_url = reverse_lazy('milkinput_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_quantity'] = sum(milkinput.milk_quantity for milkinput in self.object_list)
        return context

class MilkInputDetailView(DetailView):
    model = MilkInput
    template_name = 'milkinput_detail.html'
    success_url = reverse_lazy('milkinput_list')

class MilkInputCreateView(CreateView):
    model = MilkInput
    template_name = 'milkinput_form.html'
    fields = ['farmer', 'milk_quantity','quality']
    success_url = reverse_lazy('milkinput_list')

class MilkInputUpdateView(UpdateView):
    model = MilkInput
    template_name = 'milkinput_form.html'
    fields = ['farmer', 'milk_quantity','quality']
    success_url = reverse_lazy('milkinput_list')

class MilkInputDeleteView(DeleteView):
    model = MilkInput
    template_name = 'milkinput_confirm_delete.html'
    success_url = reverse_lazy('milkinput_list')


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
    fields = ['customer', 'order_quantity', 'status']
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'order_quantity', 'status']
    success_url = reverse_lazy('order_list')

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
    fields = ['name','quantity']
    success_url = reverse_lazy('inventory_list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventory_form.html'
    fields = ['name','quantity']
    success_url = reverse_lazy('inventory_list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['Product_Name']
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['Product_Name']

class ProductDeleteView(DeleteView):
    model = Inventory
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
# Customer Views
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['customer_name','contact_number']
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields =  ['customer_name','contact_number']
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')