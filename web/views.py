from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import RentForm

from .models import Livro, Cliente, Rent


def index(request):
    livros = Livro.objects.order_by('titulo')
    return render(request, 'web/index.html', {'livros': livros})


def estoque_livro(request):
    livros = Livro.objects.order_by('-venda')
    return render(request, 'web/estoque.html', {'livros': livros})
    # return render(request, 'web/base.html')


def descricao(request, pk):
    livro = Livro.objects.get(pk=pk)
    return render(request, 'web/descricao.html', {'livro': livro})


def lancamento_livro(request):
    return render(request, 'web/lancamento.html')


def biblioteca_livro(request):
    return render(request, 'web/biblioteca.html')



def carrinho_livro(request, pk):
     livro = Livro.objects.get(pk=pk)
     cliente = request.user
     if request.method == "POST":
         form = RentForm(request.POST)
         if form.is_valid():
          rent = form.save(commit=False)
          rent.cliente = cliente
          rent.livro = livro
          rent.save()
          return redirect('web:descricao', pk=pk)
     else:
         form = RentForm()
     return render(request, 'web/carrinho.html', {'form': form, 'cliente': cliente, 'livro': livro })        








# @login_required
# def compra(request, pkLivro, pkCliente):
#     cliente = get_object_or_404(Cliente, pkCliente =pk)
#     livro = get_object_or_404(Livro, pkLivro = pk)

#     rent = form.save(commit=False)
#     rent.cliente = cliente
#     rent.livro = livro
#     rent.data_rent = published_date__lte = timezone.now()
#     rent.data_devolucao = published_date__lte = timezone.now()
#     rent.save()
#     return render(request, 'web/index.html')

#     return render(request, 'web/carrinho.html', {'cliente': cliente, 'livro': livro})
