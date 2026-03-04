from django.db import models
from django.contrib.auth.hashers import make_password
from apps.usuarios.models import Usuario


class Aluno(models.Model):

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    matricula = models.CharField(max_length=20)

    nome = models.CharField(max_length=200)

    disciplina = models.CharField(max_length=200)

    periodo_letivo = models.CharField(max_length=20)

    turma_turno = models.CharField(max_length=50)

    grupo = models.CharField(max_length=50)

    status = models.CharField(
        max_length=20,
        default="ativo"
    )

    def save(self, *args, **kwargs):

        if not self.usuario:

            usuario, criado = Usuario.objects.get_or_create(
                matricula=self.matricula,
                defaults={
                    "username": self.matricula,
                    "perfil": "aluno",
                    "password": make_password("123456")
                }
            )

            self.usuario = usuario

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome