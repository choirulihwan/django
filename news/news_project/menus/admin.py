from django.contrib import admin

# Register your models here.
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('nama', 'menu_induk', 'link', 'icon', 'status')

    def nama(self, obj):
        return obj.name
    nama.short_description = 'NAMA'

    def menu_induk(self, obj):
        return obj.parent_id
    menu_induk.short_description = 'MENU INDUK'

    def status(self, obj):
        return obj.is_active
    status.short_description = 'AKTIF'


admin.site.register(Menu, MenuAdmin)