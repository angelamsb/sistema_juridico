from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.plantoes.models import Plantao


@login_required
def plantoes_para_avaliar(request):

    plantoes = Plantao.objects.filter(
        status="finalizado",
        status_avaliacao="pendente"
    ).order_by("data_entrada")

    return render(
        request,
        "avaliacoes/plantoes_para_avaliar.html",
        {"plantoes": plantoes}
    )