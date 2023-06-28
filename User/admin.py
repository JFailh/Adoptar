from django.contrib import admin
from User.models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("username","email","password")