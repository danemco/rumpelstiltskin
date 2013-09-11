from django.contrib import admin
from inventory.models import Item, Category

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'quantity',)

    # Question for John: how to put the category list as a filter in the admin?

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
