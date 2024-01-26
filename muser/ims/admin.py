from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(category)
admin.site.register(itemGroup)
admin.site.register(spareGroup)
admin.site.register(wareHouse)
admin.site.register(item)
admin.site.register(spareItem)
admin.site.register(takeoutOrders)
admin.site.register(crossDock)
admin.site.register(maintainableItem)
admin.site.register(damagedItem)
admin.site.register(thresholdItems)
admin.site.register(transactionReport)
admin.site.register(maintenanceHistory)
