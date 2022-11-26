from django.db import models

# Create your models here.

from django.db import models

class Cliente(models.Model):
    razaosocial = models.CharField('Razão Social', max_length=20)
    cnpj = models.CharField('CNPJ', max_length=14)
    gerenteresponsavel = models.CharField('Gerente Responsavel', max_length=30)
    telempresa = models.CharField('Telefone', max_length=12)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        def __str__(self):
            return self.nome

class Servico(models.Model):
    razaosocial = models.CharField('Razão Social', max_length=20)
    cnpj = models.CharField('CNPJ', max_length=14)
    especificacoesdoservico = models.CharField('Especificações do Serviço',max_length=200)

    class Meta:
        verbose_nome = 'Serviço'
        verbose_nome_plural = 'Serviços'

        def __str__(self):
            return self.nome