from django.contrib import admin
from Perro.models import Perro

# Register your models here.


@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ("nombre","edad","raza")