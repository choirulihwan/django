from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display = ('id', 'category', 'title', 'price', 'is_olx_published')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    # list_editable = ('is_published',)
    # search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)
