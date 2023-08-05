from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Category, ProductAccessories, ProductAlternatives

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductAlternatives)
admin.site.register(ProductAccessories)