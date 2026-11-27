from django.conf import settings
from django.db import models


class CategoriaServico(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria de serviço"
        verbose_name_plural = "Categorias de serviço"

    def __str__(self):
        return self.nome


class PerfilPrestador(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_prestador",
    )
    categoria = models.ForeignKey(
        CategoriaServico,
        on_delete=models.PROTECT,
        related_name="prestadores",
    )
    descricao = models.TextField("Descrição")
    especialidades = models.CharField(
        max_length=255,
        help_text="Separe por vírgula. Ex.: instalação elétrica, chuveiro, quadro de luz",
    )
    valor_medio = models.DecimalField(
        "Valor médio (R$)", max_digits=8, decimal_places=2, null=True, blank=True
    )
    bairros_atendidos = models.CharField(
        max_length=255,
        help_text="Separe por vírgula. Ex.: Centro, Jardim América",
    )
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["usuario__first_name", "usuario__username"]
        verbose_name = "Perfil de prestador"
        verbose_name_plural = "Perfis de prestadores"

    def __str__(self):
        return self.nome_exibicao

    @property
    def nome_exibicao(self):
        return self.usuario.get_full_name() or self.usuario.get_username()

    @property
    def lista_especialidades(self):
        return [e.strip() for e in self.especialidades.split(",") if e.strip()]

    @property
    def lista_bairros(self):
        return [b.strip() for b in self.bairros_atendidos.split(",") if b.strip()]