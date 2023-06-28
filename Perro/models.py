from django.db import models

# Create your models here.


class Perro(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    raza = models.CharField(max_length=20, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    def adoptado(self):
        self.estado = False
        super().save()

    def delete(self,*args,**kwargs):
        self.adoptado()