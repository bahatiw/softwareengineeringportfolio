from django.db import models
import random
import datetime

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
        Order.objects.create(customer=self, order_quantity=quantity, status=status)

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
    # Fields
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    member_number = models.PositiveIntegerField(unique=True, editable=False)
    date_joined = models.DateField(auto_now_add=True)
    id_number = models.FloatField()

    # Override the save method to generate a 4-digit member_number
    def save(self, *args, **kwargs):
        if not self.member_number:
            self.member_number = random.randint(1000, 9999)
            while Farmer.objects.filter(member_number=self.member_number).exists():
                self.member_number = random.randint(1000, 9999)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.second_name} - {self.member_number}"

    
class MilkInput(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    milk_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    production_date = models.DateField(auto_now_add=True)
    quality = models.CharField(max_length=50, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ])
    def save(self, *args, **kwargs):
        # Save the MilkInput instance first
        super().save(*args, **kwargs)

        # Get or create the Inventory instance
        # Update the inventory whenever a new FarmMilkInput is saved
        inventory, created = Inventory.objects.get_or_create(name='Milk')
        inventory.quantity += self.milk_quantity
        inventory.save() 

    def __str__(self):
        return f"Farmer: {self.farmer.First_Name} {self.farmer.Second_Name}, Quantity: {self.milk_quantity}, Date: {self.production_date}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    order_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Save the MilkInput instance first
        super().save(*args, **kwargs)

        # Get or create the Inventory instance
        # Update the inventory whenever a new FarmMilkInput is saved
        inventory, created = Inventory.objects.get_or_create(name='Milk')
        inventory.quantity -= self.order_quantity
        inventory.save() 

    def __str__(self):
        return f"Customer: {self.customer.customer_name}, Quantity: {self.order_quantity}, Status: {self.status}"
class Product(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"Product_Name: {self.name}"

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
 
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
