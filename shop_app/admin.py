from django.contrib import admin
from shop_app.models import Product, Category
    # Cart, Cart_product


admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Cart_product)

# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user',)
