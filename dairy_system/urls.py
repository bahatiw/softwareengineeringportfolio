from django.urls import path
from .views import (
    FarmerListView, FarmerDetailView, FarmerCreateView, FarmerUpdateView, FarmerDeleteView,
    MilkInputListView, MilkInputDetailView, MilkInputCreateView, MilkInputUpdateView, MilkInputDeleteView,
    MilkQualityListView, MilkQualityDetailView, MilkQualityCreateView, MilkQualityUpdateView, MilkQualityDeleteView,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    InventoryListView, InventoryDetailView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView,dashboard
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

    path('milkqualities/', MilkQualityListView.as_view(), name='milkquality_list'),
    path('milkquality/<int:pk>/', MilkQualityDetailView.as_view(), name='milkquality_detail'),
    path('milkquality/new/', MilkQualityCreateView.as_view(), name='milkquality_create'),
    path('milkquality/<int:pk>/edit/', MilkQualityUpdateView.as_view(), name='milkquality_edit'),
    path('milkquality/<int:pk>/delete/', MilkQualityDeleteView.as_view(), name='milkquality_delete'),

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
]
