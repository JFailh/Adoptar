from django.contrib import admin
from Gato.models import Gato
# Register your models here.


@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ("nombre","edad","raza")