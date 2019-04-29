from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, ContatoForm
from django.http import Http404, HttpResponse
from django.core.mail import send_mail, BadHeaderError

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.visits += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if not (request.user.is_authenticated()):
         return redirect('post_list')
         # raise Http404("Pagina Nao Existe")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

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
                send_mail(assunto, msg, emissor, ['mateusowmedeiros@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('obg')
    return render(request, 'blog/email.html', {'form': email_form})

def obg(request):
    return HttpResponse("<h2>Obrigado pela mensagem!!!</h2>")