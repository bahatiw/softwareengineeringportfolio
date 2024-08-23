from django.contrib import admin
from .models import Role,MilkQualityRole,FrontOffice,Customer,Manager,Farmer,MilkInput,MilkQuality,Order,Inventory
# Register your models here.
admin.site.register(Role)
admin.site.register(MilkQualityRole)
admin.site.register(FrontOffice)
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Farmer)
admin.site.register(MilkInput)
admin.site.register(MilkQuality)
admin.site.register(Order)
admin.site.register(Inventory)