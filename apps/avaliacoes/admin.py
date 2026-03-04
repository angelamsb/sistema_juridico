from django.contrib import admin
from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):

    fieldsets = (

        ("PLANTÃO", {
            "fields": ("plantao",)
        }),

        ("CRITÉRIO 1", {
            "fields": ("N1", "N2", "N3", "N4", "SUM1")
        }),

        ("CRITÉRIO 2", {
            "fields": ("N5", "N6", "N7", "N8", "SUM2")
        }),

        ("CRITÉRIO 3", {
            "fields": ("N9", "N10", "N11", "N12", "SUM3")
        }),

        ("CRITÉRIO 4", {
            "fields": ("N13", "N14", "N15", "N16", "SUM4")
        }),

        ("CRITÉRIO 5", {
            "fields": ("N17", "N18", "N19", "N20", "SUM5")
        }),

        ("RESULTADO FINAL", {
            "fields": ("nota_final", "data_avaliacao")
        }),

    )

    readonly_fields = (
        "SUM1",
        "SUM2",
        "SUM3",
        "SUM4",
        "SUM5",
        "nota_final",
    )