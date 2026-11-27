from django import forms

from .models import CategoriaServico


class BuscaPrestadorForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Buscar",
        widget=forms.TextInput(
            attrs={"placeholder": "Nome, serviço ou especialidade", "class": "form-control"}
        ),
    )
    categoria = forms.ModelChoiceField(
        queryset=CategoriaServico.objects.all(),
        required=False,
        empty_label="Todas as categorias",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    bairro = forms.CharField(
        required=False,
        label="Bairro",
        widget=forms.TextInput(attrs={"placeholder": "Bairro", "class": "form-control"}),
    )