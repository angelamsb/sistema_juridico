from django.contrib import admin
from django.urls import path, include
from apps.relatorios.views import dashboard
from apps.relatorios.views import relatorio_avaliacoes_pdf

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/', dashboard, name='dashboard'),

    path('plantoes/', include('apps.plantoes.urls')),
    
    path('aluno/', include('apps.alunos.urls')),
    path('avaliacoes/', include('apps.avaliacoes.urls')),
    path('relatorios/avaliacoes/pdf/', relatorio_avaliacoes_pdf, name='relatorio_pdf'),
]