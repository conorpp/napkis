
from django.contrib import admin
from napkis.apps.menu.models import MenuItem, Employee, Menu, Order, Group

    
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    name = 'Menu Item'
    class Meta():
        verbose_name = 'Menu Items'
    
class MenuAdmin(admin.ModelAdmin):
    inlines=[MenuItemInline,]
    search_fields = ['name','price']
    #ordering = ['-created']

admin.site.register(Menu,MenuAdmin)
admin.site.register(MenuItem)
