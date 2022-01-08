from django.contrib import admin

# Register your models here.
from .models import Store


# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'olx_id', 'shopee_id', 'tokopedia_id', 'instagram_id')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    # list_editable = ('is_mvp',)

admin.site.register(Store, StoreAdmin)