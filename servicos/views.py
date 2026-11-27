from django.db.models import Q
from django.views.generic import DetailView, ListView

from .forms import BuscaPrestadorForm
from .models import PerfilPrestador


class PrestadorListView(ListView):
    model = PerfilPrestador
    template_name = "servicos/lista_prestadores.html"
    context_object_name = "prestadores"
    paginate_by = 9

    def get_queryset(self):
        qs = PerfilPrestador.objects.filter(ativo=True).select_related(
            "usuario", "categoria"
        )
        self.form = BuscaPrestadorForm(self.request.GET or None)

        if self.form.is_valid():
            q = self.form.cleaned_data.get("q")
            categoria = self.form.cleaned_data.get("categoria")
            bairro = self.form.cleaned_data.get("bairro")

            if q:
                qs = qs.filter(
                    Q(usuario__first_name__icontains=q)
                    | Q(usuario__last_name__icontains=q)
                    | Q(usuario__username__icontains=q)
                    | Q(descricao__icontains=q)
                    | Q(especialidades__icontains=q)
                    | Q(categoria__nome__icontains=q)
                )
            if categoria:
                qs = qs.filter(categoria=categoria)
            if bairro:
                qs = qs.filter(bairros_atendidos__icontains=bairro)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = self.form
        params = self.request.GET.copy()
        params.pop("page", None)
        ctx["querystring"] = params.urlencode()
        return ctx


class PrestadorDetailView(DetailView):
    model = PerfilPrestador
    template_name = "servicos/detalhe_prestador.html"
    context_object_name = "prestador"

    def get_queryset(self):
        return PerfilPrestador.objects.filter(ativo=True).select_related(
            "usuario", "categoria"
        )