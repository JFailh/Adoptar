from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telefono= models.IntegerField(null=True,blank=True)
    email = models.EmailField('Correo electrónico', unique=True)


    def str(self):
        return self.username