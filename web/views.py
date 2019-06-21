from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from .forms import AluguelForm, UserRegisterForm, ContatoForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from .models import Livro, Cliente, Aluguel


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


def carrinho(request):
    livros = Aluguel.objects.order_by('data_aluguel')
    livrosDetail = Livro.objects.filter(pk=Aluguel.livro)

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

    livros = Aluguel.objects.order_by('data_aluguel')
    livrosDetail = Livro.objects.filter(Livro.id = Aluguel.livro)

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
                send_mail(assunto, msg, emissor, [
                          'mateusowmedeiros@gmail.com'])
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
