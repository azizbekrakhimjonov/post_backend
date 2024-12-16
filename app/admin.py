from django.contrib import admin
from .models import *

admin.site.register(Malumot)
@admin.register(Post)
class UniversitetAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'manzil', 'code')
