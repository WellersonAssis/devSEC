from django.db import models

# Create your models here.

from django.db import models

class Cliente(models.Model):
    razaosocial = models.CharField('razaosocial', max_length=20)
    cnpj = models.CharField('cnpj', max_length=14)
    gerenteresponsavel = models.CharField('gerenteresponsavel', max_length=30)
    telempresa = models.CharField('Telefone', max_length=12)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        def __str__(self):
            return self.nome