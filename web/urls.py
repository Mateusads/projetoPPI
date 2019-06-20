from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('maisvendidos/', views.mais_vendido, name='mais_vendido'),
    path('descricao/<int:pk>/', views.descricao, name='descricao'),
    path('lancamento/', views.lancamento_livro, name='lancamento_livro'),
    path('biblioteca/', views.biblioteca_livro, name='biblioteca_livro'),
    path('carrinho/<int:pk>/', views.carrinho_livro, name='carrinho_livro'),
    path('generolivro/<int:pk>/', views.genero_livro, name='genero_livro'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),

]