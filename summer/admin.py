from django.contrib import admin
from .models import Item, OrderItem, Order

# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'slug']
# 	prepopulated_fields = {'slug': ('name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
# 	list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
# 	list_filter = ['in_stock', 'is_active']
# 	list_editable = ['price', 'in_stock']
# 	prepopulated_fields = {'slug': ('title',)}

