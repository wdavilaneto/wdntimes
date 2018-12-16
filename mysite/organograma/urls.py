from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<int:projeto_id>', views.projeto, name='projeto'),
    path('<int:orgao_id>/', views.times, name='times'),
    path('<int:orgao_id>/time/', views.time, name='time'),
    path('artigos/', views.artigos, name='artigos'),
    path('artigos/<int:artigo_id>', views.artigo, name='artigo'),
    path('demandas/', views.demandas, name='demandas'),
    path('demandas/<int:demanda_id>', views.demanda, name='demanda'),
    path('perfil/<int:perfil_id>', views.perfil, name='perfil'),
    path('agil/', views.agil, name='agil'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
