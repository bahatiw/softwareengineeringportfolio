import os
import django
import random

# Set up Django environment
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DLMCSPSE01.settings')
django.setup()

from dairy_system.models import Farmer

def create_dummy_farmers():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'James', 'Anna', 'Robert', 'Laura']
    second_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez']

    for i in range(10):  # Creating 10 dummy farmers
        first_name = random.choice(first_names)
        second_name = random.choice(second_names)
        member_number = random.randint(1000, 9999)  # 4-digit unique integer
        id_number = random.uniform(100000.0, 999999.0)  # Random float for ID_Number

        farmer, created = Farmer.objects.get_or_create(
            first_name=first_name,
            second_name=second_name,
            member_number=member_number,
            id_number=id_number
        )

        if created:
            print(f'Created Farmer: {farmer.first_name} {farmer.second_name}, Member Number: {farmer.member_number}')
        else:
            print(f'Farmer already exists: {farmer.first_name} {farmer.second_name}, Member Number: {farmer.member_number}')



from dairy_system.models import Inventory, Product

def create_dummy_inventory():
    # Ensure 'Milk' product exists in the Product table
    milk_product, created = Product.objects.get_or_create(name='Milk')

    # Create a new inventory record with quantity 0
    inventory, created = Inventory.objects.get_or_create(name=milk_product, defaults={'quantity': 0.00})

    if created:
        print(f'Inventory record created: {inventory.name.name} with quantity {inventory.quantity}')
    else:
        print(f'Inventory record already exists: {inventory.name.name} with quantity {inventory.quantity}')

from dairy_system.models import MilkInput
from decimal import Decimal

def create_dummy_milk_inputs():
    # Get all farmers from the database
    farmers = Farmer.objects.all()

    if not farmers.exists():
        print("No farmers found in the database. Please add farmers first.")
        return

    # Define possible quality values
    quality_choices = ['High', 'Medium', 'Low']

    # Generate random milk inputs for each farmer
    for farmer in farmers:
        for _ in range(random.randint(1, 5)):  # Create 1 to 5 milk inputs per farmer
            milk_quantity = Decimal(random.uniform(10.0, 100.0)).quantize(Decimal('0.01'))  # Ensure it's a Decimal with 2 decimal places
            quality = random.choice(quality_choices)  # Random quality value

            milk_input = MilkInput.objects.create(
                farmer=farmer,
                milk_quantity=milk_quantity,
                quality=quality
            )

            print(f"Created Milk Input: Farmer: {farmer.first_name} {farmer.second_name}, Quantity: {milk_input.milk_quantity}, Quality: {milk_input.quality}")

if __name__ == '__main__':
    create_dummy_inventory()
    create_dummy_farmers()
    create_dummy_milk_inputs()
