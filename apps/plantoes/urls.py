from django.urls import path
from .views import novo_plantao, meus_plantoes, editar_plantao, finalizar_plantao

urlpatterns = [
    path("novo/", novo_plantao, name="novo_plantao"),
    path("meus/", meus_plantoes, name="meus_plantoes"),
    path("editar/<int:plantao_id>/", editar_plantao, name="editar_plantao"),
    path("finalizar/<int:plantao_id>/", finalizar_plantao, name="finalizar_plantao"),
]
