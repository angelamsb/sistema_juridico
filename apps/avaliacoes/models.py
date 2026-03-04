from django.db import models
from apps.plantoes.models import Plantao


class Avaliacao(models.Model):

    plantao = models.ForeignKey(
        Plantao,
        on_delete=models.CASCADE
    )

    # CRITÉRIO 1
    N1 = models.FloatField(null=True, blank=True)
    N2 = models.FloatField(null=True, blank=True)
    N3 = models.FloatField(null=True, blank=True)
    N4 = models.FloatField(null=True, blank=True)

    SUM1 = models.FloatField(null=True, blank=True)

    # CRITÉRIO 2
    N5 = models.FloatField(null=True, blank=True)
    N6 = models.FloatField(null=True, blank=True)
    N7 = models.FloatField(null=True, blank=True)
    N8 = models.FloatField(null=True, blank=True)

    SUM2 = models.FloatField(null=True, blank=True)

    # CRITÉRIO 3
    N9 = models.FloatField(null=True, blank=True)
    N10 = models.FloatField(null=True, blank=True)
    N11 = models.FloatField(null=True, blank=True)
    N12 = models.FloatField(null=True, blank=True)

    SUM3 = models.FloatField(null=True, blank=True)

    # CRITÉRIO 4
    N13 = models.FloatField(null=True, blank=True)
    N14 = models.FloatField(null=True, blank=True)
    N15 = models.FloatField(null=True, blank=True)
    N16 = models.FloatField(null=True, blank=True)

    SUM4 = models.FloatField(null=True, blank=True)

    # CRITÉRIO 5
    N17 = models.FloatField(null=True, blank=True)
    N18 = models.FloatField(null=True, blank=True)
    N19 = models.FloatField(null=True, blank=True)
    N20 = models.FloatField(null=True, blank=True)

    SUM5 = models.FloatField(null=True, blank=True)

    nota_final = models.FloatField(null=True, blank=True)

    data_avaliacao = models.DateField(auto_now_add=True)

    def validar_nota(self, nota):
        if nota is None:
            return 0
        if nota > 2:
            raise ValueError("Nota não pode ser maior que 2.0")
        return nota

    def save(self, *args, **kwargs):

        n1 = self.validar_nota(self.N1)
        n2 = self.validar_nota(self.N2)
        n3 = self.validar_nota(self.N3)
        n4 = self.validar_nota(self.N4)

        n5 = self.validar_nota(self.N5)
        n6 = self.validar_nota(self.N6)
        n7 = self.validar_nota(self.N7)
        n8 = self.validar_nota(self.N8)

        n9 = self.validar_nota(self.N9)
        n10 = self.validar_nota(self.N10)
        n11 = self.validar_nota(self.N11)
        n12 = self.validar_nota(self.N12)

        n13 = self.validar_nota(self.N13)
        n14 = self.validar_nota(self.N14)
        n15 = self.validar_nota(self.N15)
        n16 = self.validar_nota(self.N16)

        n17 = self.validar_nota(self.N17)
        n18 = self.validar_nota(self.N18)
        n19 = self.validar_nota(self.N19)
        n20 = self.validar_nota(self.N20)

        self.SUM1 = n1 + n2 + n3 + n4
        self.SUM2 = n5 + n6 + n7 + n8
        self.SUM3 = n9 + n10 + n11 + n12
        self.SUM4 = n13 + n14 + n15 + n16
        self.SUM5 = n17 + n18 + n19 + n20

        self.nota_final = (
            self.SUM1 +
            self.SUM2 +
            self.SUM3 +
            self.SUM4 +
            self.SUM5
        )

        super().save(*args, **kwargs)

        # marcar plantão como avaliado
        self.plantao.status_avaliacao = "avaliado"
        self.plantao.save()

    def __str__(self):
        return f"Avaliação Plantão {self.plantao.id}"