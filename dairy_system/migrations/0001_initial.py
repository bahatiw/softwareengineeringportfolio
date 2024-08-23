# Generated by Django 5.1 on 2024-08-19 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('contact_number', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_info', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FrontOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MilkQualityRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat_content', models.FloatField()),
                ('protein_content', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Farmer', 'Farmer'), ('Admin', 'Admin'), ('Manager', 'Manager'), ('Front_office', 'Front Office'), ('Quality_Inspector', 'Quality Inspector')], max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MilkInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milk_quantity', models.FloatField()),
                ('production_date', models.DateField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairy_system.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='MilkQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat_content', models.FloatField()),
                ('protein_content', models.FloatField()),
                ('testing_date', models.DateField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairy_system.farmer')),
                ('quality_inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.FloatField()),
                ('status', models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=50)),
                ('order_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairy_system.customer')),
            ],
        ),
    ]
