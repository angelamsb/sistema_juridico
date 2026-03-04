from django.urls import path
from .views import plantoes_para_avaliar

urlpatterns = [
    path(
        "plantoes/",
        plantoes_para_avaliar,
        name="plantoes_para_avaliar"
    ),
]