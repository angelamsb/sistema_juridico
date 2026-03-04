from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PlantaoForm
from .models import Plantao
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required
def editar_plantao(request, plantao_id):

    plantao = get_object_or_404(
        Plantao,
        id=plantao_id,
        aluno=request.user.aluno
    )

    # Regra: só editar se estiver aberto
    if plantao.status != "aberto":
        return HttpResponseForbidden("Este plantão não pode mais ser editado.")

    if request.method == "POST":
        form = PlantaoForm(request.POST, instance=plantao)
        if form.is_valid():
            form.save()
            return redirect("meus_plantoes")
    else:
        form = PlantaoForm(instance=plantao)

    return render(
        request,
        "plantoes/editar_plantao.html",
        {"form": form, "plantao": plantao}
    )

@login_required
def novo_plantao(request):

    if request.method == "POST":

        form = PlantaoForm(request.POST)

        if form.is_valid():

            plantao = form.save(commit=False)

            plantao.aluno = request.user.aluno

            plantao.save()

            return redirect("meus_plantoes")

    else:

        form = PlantaoForm()

    return render(request, "plantoes/novo_plantao.html", {"form": form})



@login_required
def finalizar_plantao(request, plantao_id):

    plantao = get_object_or_404(
        Plantao,
        id=plantao_id,
        aluno=request.user.aluno
    )

    if plantao.status != "aberto":
        return HttpResponseForbidden("Este plantão já foi finalizado.")

    plantao.status = "finalizado"
    plantao.save()

    return redirect("meus_plantoes")

@login_required
def meus_plantoes(request):

    plantoes = Plantao.objects.filter(
        aluno=request.user.aluno
    ).order_by("numero_plantao")

    return render(
        request,
        "plantoes/meus_plantoes.html",
        {"plantoes": plantoes}
    )