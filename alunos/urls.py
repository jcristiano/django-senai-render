from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('lista/', views.lista_alunos, name='lista_alunos'),
]