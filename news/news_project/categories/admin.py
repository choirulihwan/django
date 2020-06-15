from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

    def category(self, obj):
        return obj.cat_name
    category.short_description = 'Category'


admin.site.register(Category, CategoryAdmin)
