from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Cliente, Servico
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('razaosocial','cnpj','gerenteresponsavel','telempresa')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('razaosocial','cnpj','esécificacoesdoservico')
