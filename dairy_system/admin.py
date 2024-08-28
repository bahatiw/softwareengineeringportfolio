from django.contrib import admin
from .models import Role,FrontOffice,Customer,Manager,Farmer,MilkInput,Order,Inventory
# Register your models here.
admin.site.register(Role)
admin.site.register(FrontOffice)
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Farmer)
admin.site.register(MilkInput)
admin.site.register(Order)
admin.site.register(Inventory)