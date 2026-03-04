from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    PERFIL_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('SUPERVISOR', 'Supervisor'),
        ('SECRETARIA', 'Secretaria'),
        ('ALUNO', 'Aluno'),
        ('AVALIADOR', 'Avaliador'),
    ]

    matricula = models.CharField(max_length=20, unique=True)

    perfil = models.CharField(
        max_length=20,
        choices=PERFIL_CHOICES
    )

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username