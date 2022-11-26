from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Cliente, Servico, Contrato, Endereco, Funcionario, Manutencao


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('razaosocial', 'cnpj', 'gerenteresponsavel', 'telempresa')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('razaosocial', 'cnpj', 'especificacoesdoservico')


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('numcontrato', 'servicocontratado')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logadouro', 'cep', 'uf', 'numestabelecimento')



@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('desenvolvedorlider', 'desenvolvedoresauxiliares')


@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('horamanutencao', 'desenvolvedorresponsavel')
