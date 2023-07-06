from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','product_image','description')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)
