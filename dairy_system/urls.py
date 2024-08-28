from django.urls import path
from .views import (
    FarmerListView, FarmerDetailView, FarmerCreateView, FarmerUpdateView, FarmerDeleteView,
    MilkInputListView, MilkInputDetailView, MilkInputCreateView, MilkInputUpdateView, MilkInputDeleteView, 
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    InventoryListView, InventoryDetailView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView,dashboard,
    ProductCreateView, ProductListView, ProductDeleteView, ProductDetailView,ProductUpdateView,CustomerListView,CustomerCreateView,
    CustomerDeleteView,CustomerDetailView,CustomerUpdateView
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('farmers/', FarmerListView.as_view(), name='farmer_list'),
    path('farmer/<int:pk>/', FarmerDetailView.as_view(), name='farmer_detail'),
    path('farmer/new/', FarmerCreateView.as_view(), name='farmer_create'),
    path('farmer/<int:pk>/edit/', FarmerUpdateView.as_view(), name='farmer_edit'),
    path('farmer/<int:pk>/delete/', FarmerDeleteView.as_view(), name='farmer_delete'),

    path('milkinputs/', MilkInputListView.as_view(), name='milkinput_list'),
    path('milkinput/<int:pk>/', MilkInputDetailView.as_view(), name='milkinput_detail'),
    path('milkinput/new/', MilkInputCreateView.as_view(), name='milkinput_create'),
    path('milkinput/<int:pk>/edit/', MilkInputUpdateView.as_view(), name='milkinput_edit'),
    path('milkinput/<int:pk>/delete/', MilkInputDeleteView.as_view(), name='milkinput_delete'),

    
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/new/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    path('inventories/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/new/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory_edit'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/new/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),


]
