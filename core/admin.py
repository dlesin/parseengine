from django.contrib import admin
from .models import *


admin.site.register(Contact)




# class OrderAdmin (admin.ModelAdmin):
#     #list_display = ["name", "email"]
#     list_display = [field.name for field in Order._meta.fields]
#     filter_vertical = ('items'),
#     #inlines = [CartInline]
#
#     class Meta:
#         model = Order
#
# admin.site.register(Order, OrderAdmin)
