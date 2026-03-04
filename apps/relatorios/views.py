from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from apps.alunos.models import Aluno
from apps.plantoes.models import Plantao
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from apps.avaliacoes.models import Avaliacao


def relatorio_avaliacoes_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_avaliacoes.pdf"'

    pdf = canvas.Canvas(response)

    y = 800

    pdf.setFont("Helvetica", 12)
    pdf.drawString(200, y, "Relatório de Avaliações")

    y -= 40

    avaliacoes = Avaliacao.objects.select_related("plantao", "plantao__aluno")

    for avaliacao in avaliacoes:

        aluno = avaliacao.plantao.aluno.nome
        plantao = avaliacao.plantao.numero_plantao
        nota = avaliacao.nota_final

        texto = f"Aluno: {aluno} | Plantão: {plantao} | Nota Final: {nota}"

        pdf.drawString(50, y, texto)

        y -= 20

        if y < 100:
            pdf.showPage()
            y = 800

    pdf.save()

    return response

@login_required
def dashboard(request):

    total_alunos = Aluno.objects.count()

    total_plantoes = Plantao.objects.count()

    plantoes_finalizados = Plantao.objects.filter(
        status="finalizado"
    ).count()

    plantoes_avaliados = Plantao.objects.filter(
        status_avaliacao="avaliado"
    ).count()

    plantoes_pendentes = Plantao.objects.filter(
        status_avaliacao="pendente"
    ).count()

    # gráfico por grupo
    grupos = (
        Aluno.objects
        .values("grupo")
        .annotate(total=Count("grupo"))
        .order_by("grupo")
    )

    context = {
        "total_alunos": total_alunos,
        "total_plantoes": total_plantoes,
        "plantoes_finalizados": plantoes_finalizados,
        "plantoes_avaliados": plantoes_avaliados,
        "plantoes_pendentes": plantoes_pendentes,
        "grupos": list(grupos)
    }

    return render(request, "relatorios/dashboard.html", context)