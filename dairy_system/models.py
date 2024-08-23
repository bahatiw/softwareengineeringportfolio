from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Role(models.Model):
    FARMER = 'Farmer'
    ADMIN = 'Admin'
    MANAGER = 'Manager'
    FRONT_OFFICE = 'Front_office'
    QUALITY_INSPECTOR = 'Quality_Inspector'

    ROLE_CHOICES = [
        (FARMER, 'Farmer'),
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (FRONT_OFFICE, 'Front Office'),
        (QUALITY_INSPECTOR, 'Quality Inspector'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class MilkQualityRole(models.Model):
    fat_content = models.FloatField()
    protein_content = models.FloatField()

    def __str__(self):
        return f"Fat: {self.fat_content}, Protein: {self.protein_content}"

class FrontOffice(models.Model):
    def create_farmer(self, name, contact):
        Farmer.objects.create(name=name, contact_info=contact)

    def delete_farmer(self, farmer_id):
        Farmer.objects.filter(id=farmer_id).delete()

    def input_milk_delivery(self, farmer, quantity, date):
        MilkInput.objects.create(farmer=farmer, milk_quantity=quantity, production_date=date)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    contact_number = models.FloatField()

    def place_order(self, quantity, status, date):
        Order.objects.create(customer=self, order_quantity=quantity, status=status, order_date=date)

    def receive_order(self, order_id):
        order = Order.objects.get(id=order_id)
        order.status = 'Delivered'
        order.save()

class Manager(models.Model):
    def view_order(self, order_id):
        return Order.objects.get(id=order_id)

    def check_inventory(self):
        return Inventory.objects.all()

class Farmer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.FloatField()

    def input_milk_supply(self, quantity, date):
        MilkInput.objects.create(farmer=self, milk_quantity=quantity, production_date=date)

    def view_milk_supplied(self):
        return MilkInput.objects.filter(farmer=self)

class MilkInput(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    milk_quantity = models.FloatField()
    production_date = models.DateField()

    def __str__(self):
        return f"Farmer: {self.farmer.name}, Quantity: {self.milk_quantity}, Date: {self.production_date}"

class MilkQuality(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    fat_content = models.FloatField()
    protein_content = models.FloatField()
    testing_date = models.DateField()
    quality_inspector = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Farmer: {self.farmer.name}, Fat: {self.fat_content}, Protein: {self.protein_content}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_quantity = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    order_date = models.DateField()

    def __str__(self):
        return f"Customer: {self.customer.customer_name}, Quantity: {self.order_quantity}, Status: {self.status}"

class Inventory(models.Model):
    quantity = models.FloatField()
    updated_at = models.DateField()

    def increase_quantity(self, amount):
        self.quantity += amount
        self.updated_at = models.DateField(auto_now=True)
        self.save()

    def decrease_quantity(self, amount):
        self.quantity -= amount
        self.updated_at = models.DateField(auto_now=True)
        self.save()

    def __str__(self):
        return f"Quantity: {self.quantity}, Updated At: {self.updated_at}"
