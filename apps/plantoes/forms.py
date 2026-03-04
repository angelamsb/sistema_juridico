from django import forms
from .models import Plantao


class PlantaoForm(forms.ModelForm):

    class Meta:
        model = Plantao

        fields = [
            "data_entrada",
            "hora_entrada",
            "hora_saida",
            "assistido",
            "publicacoes",
            "procedimento",
            "movimentacao_processual",
            "observacoes",
            "numero_processo",
        ]