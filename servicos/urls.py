from django.urls import path

from . import views

app_name = "servicos"

urlpatterns = [
    path("", views.PrestadorListView.as_view(), name="lista_prestadores"),
    path("prestador/<int:pk>/", views.PrestadorDetailView.as_view(), name="detalhe_prestador"),
]