from django.db import models

# Create your models here.

from django.db import models

from stdimage.models import StdImageField

import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]

    filename = f'{uuid.uuid4()}.{ext}'

    return filename

class Cliente(models.Model):
    razaosocial = models.CharField('Razão Social', max_length=20)
    cnpj = models.CharField('CNPJ', max_length=14)
    gerenteresponsavel = models.CharField('Gerente Responsavel', max_length=30)
    telempresa = models.CharField('Telefone', max_length=12)
    imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,
                           variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

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
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

        def __str__(self):
            return self.nome


class Contrato (models.Model):
    numcontrato = models.CharField('Numero do Contrato', max_length=20)
    servicocontratado = models.TextField('Serviço', max_length=100)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

        def __str__(self):
            return self.nome

class Endereco (models.Model):
    logadouro = models.CharField('Rua,Avenida', max_length=50)
    cep = models.CharField('Cep', max_length=9)
    uf = models.CharField('Uf', max_length=2)
    numestabelecimento = models.CharField('N°', max_length=6)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

        def __str__(self):
            return self.nome


    class Meta:
        verbose_name = 'Reunião'
        verbose_name_plural = 'Reunião'

        def __str__(self):
            return self.nome

class Funcionario (models.Model):
    desenvolvedorlider = models.CharField('Lider', max_length=30)
    desenvolvedoresauxiliares = models.CharField('Auxilíares', max_length=30)
    imagem = StdImageField('Imagem', null=True, blank=True, upload_to=get_file_path,
                           variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})


    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

        def __str__(self):
            return self.nome

class Manutencao (models.Model):
    horamanutencao = models.CharField('Horário de manutenção', max_length=10)
    desenvolvedorresponsavel = models.CharField('Desenvolvedor Responsável', max_length=30)

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'

    def __str__(self):
        return self.nome