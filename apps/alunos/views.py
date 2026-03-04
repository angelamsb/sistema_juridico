from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.plantoes.models import Plantao


@login_required
def painel_aluno(request):

    aluno = request.user.aluno

    plantoes = Plantao.objects.filter(
        aluno=aluno
    ).order_by("numero_plantao")

    context = {
        "plantoes": plantoes
    }

    return render(request, "alunos/painel_aluno.html", context)
