from django.db import models

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    CATEGORIA_CHOICES = (
        ('Basico', 'Basico'),
        ('Premium', 'Premium'),
    )

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.nombre
