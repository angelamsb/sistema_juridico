from django.db import models
from apps.alunos.models import Aluno


class Plantao(models.Model):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    numero_plantao = models.IntegerField(
        editable=False
    )

    data_entrada = models.DateField()

    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()

    assistido = models.TextField()

    publicacoes = models.TextField(blank=True, null=True)
    procedimento = models.TextField(blank=True, null=True)
    movimentacao_processual = models.TextField(blank=True, null=True)

    observacoes = models.TextField(blank=True, null=True)

    numero_processo = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default="aberto"
    )

    status_avaliacao = models.CharField(
        max_length=20,
        default="pendente"
    )

    def save(self, *args, **kwargs):

        # contar quantos plantões já existem para o aluno
        total = Plantao.objects.filter(aluno=self.aluno).count()

        # se for um novo plantão
        if not self.pk:

            # limitar a 10
            if total >= 10:
                raise ValueError("Este aluno já possui 10 plantões.")

            # verificar último plantão
            ultimo = Plantao.objects.filter(
                aluno=self.aluno
            ).order_by('-numero_plantao').first()

            if ultimo:
                if ultimo.status != "finalizado":
                    raise ValueError(
                        "O plantão anterior precisa estar finalizado."
                    )

                self.numero_plantao = ultimo.numero_plantao + 1
            else:
                # primeiro plantão
                self.numero_plantao = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.aluno.nome} - Plantão {self.numero_plantao}"