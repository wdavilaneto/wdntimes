from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<int:projeto_id>', views.projeto, name='projeto'),
    path('<int:orgao_id>/', views.detail, name='detail'),
    path('<int:orgao_id>/time/', views.time, name='time'),
]
