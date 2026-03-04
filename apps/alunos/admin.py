from django.contrib import admin
from .models import Aluno
from apps.plantoes.models import Plantao


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = (
        "matricula",
        "nome",
        "disciplina",
        "turma_turno",
        "periodo_letivo",
        "grupo",
        "plantao_total",
        
    )
     
    list_filter = (
        "grupo",
        "periodo_letivo",
    ) 
    def plantao_total(self, obj):

        total = Plantao.objects.filter(aluno=obj).count()

        return f"{total} / 10"

    plantao_total.short_description = "Plantões"