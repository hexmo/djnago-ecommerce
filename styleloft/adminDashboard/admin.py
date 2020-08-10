from django.contrib import admin
from .models import *

# Registered our models here to be viewed in django admin dashboard

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order)
