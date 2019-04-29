from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('estoque/', views.estoque_livro, name='estoque_livro'),
    path('descricao/<int:pk>/', views.descricao, name='descricao'),
    path('lancamento/', views.lancamento_livro, name='lancamento_livro'),
    path('biblioteca/', views.biblioteca_livro, name='biblioteca_livro'),
    path('carrinho/<int:pk>/', views.carrinho_livro, name='carrinho_livro'),

]