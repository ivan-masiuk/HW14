from django.contrib import admin

# Register your models here.

from product.models import (Product,
                            MyCart)


# admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = list_display_links + ('price', 'quantity', 'company', 'category', 'is_active')
    list_filter = ('is_active', 'company')
    search_fields = ('company',)
    actions = ('activate_products', 'deactivate_products')
    readonly_fields = ('id', 'company')


admin.site.register(Product, ProductAdmin)

admin.site.register(MyCart)
