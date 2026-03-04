from django.urls import path
from .views import painel_aluno

urlpatterns = [
    path("painel/", painel_aluno, name="painel_aluno"),
]