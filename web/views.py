from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from .forms import AluguelForm, UserRegisterForm, ContatoForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db import connection
from django.contrib import messages
from django.core import serializers
import json

from .models import Livro, Cliente, Aluguel, Carrinho


def index(request):
    message = messages.get_messages(request)
    livros = Livro.objects.order_by('titulo')
    return render(request, 'web/index.html', {'livros': livros, "message":message})


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


@login_required
def carrinho(request):
    livros = Aluguel.objects.filter(cliente=request.user)
    livrosDetail = Carrinho.objects.all()
    return render(request, 'web/carrinho.html', {'livrosDetail': livrosDetail, 'livros': livros})


@login_required
def carrinho_livro(request, pk):
    livro = Livro.objects.get(pk=pk)
    cliente = request.user

    aluguel = Aluguel()
    aluguel.cliente = cliente
    aluguel.livro = livro
    aluguel.data_aluguel = timezone.now()
    aluguel.data_devolucao = timezone.now()
    aluguel.save()

    c = Carrinho(status='Espera')
    c.save()
    c.livro.add(livro)

    livros = Aluguel.objects.filter(cliente=request.user)
    livrosDetail = Carrinho.objects.all()
    # livrosDetail = Carrinho.objects.prefetch_related('livros').all()

    return render(request, 'web/carrinho.html', {'livrosDetail': livrosDetail, 'livros': livros})


@login_required
def perfil(request):
    cliente = request.user
    return render(request, 'web/perfil.html', {'cliente': cliente})


def contato(request):
    if request.method == 'GET':
        email_form = ContatoForm()
    else:
        email_form = ContatoForm(request.POST)
        if email_form.is_valid():
            emissor = email_form.cleaned_data['emissor']
            assunto = email_form.cleaned_data['assunto']
            msg = email_form.cleaned_data['msg']

            try:

                messages.success(request, 'Mensagem enviada com Sucesso!!!', extra_tags='alert')
                # send_mail(assunto, msg, emissor, [
                #           'mateusowmedeiros@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('/')
    return render(request, 'web/contato.html', {'form': email_form})


def obg(request):
    return HttpResponse("<h2>Obrigado pela mensagem!!!</h2>")


class SignUp(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def search(request):
    titulo = request.GET.get('titulo')
    livros = Livro.objects.filter(titulo=titulo)    
    livros = [ livro_serializer(livro) for livro in livros ]


    return HttpResponse(json.dumps(livros), content_type='application/json' )


def livro_serializer(livro):
    return {'id': livro.id, 'titulo': livro.titulo, 'description': livro.descricao}