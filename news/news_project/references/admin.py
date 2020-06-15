from django.contrib import admin

from .models import Referensi

# Register your models here.
class ReferensiAdmin(admin.ModelAdmin):
    list_display = ('id_ref', 'no_ref', 'keterangan', 'keterangan_label')

admin.site.register(Referensi, ReferensiAdmin)
