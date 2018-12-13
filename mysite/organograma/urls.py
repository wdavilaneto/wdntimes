from django.urls import path

from . import views


urlpatterns = [
    # ex: /organograma/
    path('', views.index, name='index'),
    # ex: /organograma/5/
    path('<int:orgao_id>/', views.detail, name='detail'),
    # ex: /organograma/5/results/
    path('<int:orgao_id>/results/', views.results, name='results'),
    # ex: /organograma/5/vote/
    path('<int:orgao_id>/time/', views.time, name='time'),
]
