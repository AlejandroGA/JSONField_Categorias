from django.contrib import admin
from .models import Servicios

# Register your models here.
@admin.register(Servicios)
class CasaAdmin(admin.ModelAdmin):
    pass
