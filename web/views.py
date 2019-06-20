from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import RentForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm

from .models import Livro, Cliente, Rent


def index(request):
    livros = Livro.objects.order_by('titulo')
    return render(request, 'web/index.html', {'livros': livros})


def mais_vendido(request):
    livros = Livro.objects.order_by('-venda')
    

    return render(request, 'web/estoque.html', {'livros': livros})


def descricao(request, pk):
    livro = Livro.objects.get(pk=pk)
    return render(request, 'web/descricao.html', {'livro': livro})


def lancamento_livro(request):
    return render(request, 'web/lancamento.html')


def biblioteca_livro(request):
    return render(request, 'web/biblioteca.html')

def genero_livro(request, pk):
    # id = Livro.objects.get(pk=pk)
   
    livros = Livro.objects.filter(genero=pk)

    return render(request, 'web/genero.html', {'livros': livros})



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


class SignUp(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'





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
