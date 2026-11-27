from django.contrib import admin

from .models import CategoriaServico, PerfilPrestador


@admin.register(CategoriaServico)
class CategoriaServicoAdmin(admin.ModelAdmin):
    search_fields = ["nome"]


@admin.register(PerfilPrestador)
class PerfilPrestadorAdmin(admin.ModelAdmin):
    list_display = ["nome_exibicao", "categoria", "valor_medio", "ativo"]
    list_filter = ["categoria", "ativo"]
    search_fields = ["usuario__username", "usuario__first_name", "especialidades"]