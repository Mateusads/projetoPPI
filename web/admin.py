from django.contrib import admin
from .models import Livro, Cliente, Aluguel

# Register your models here.

admin.site.register(Livro)
admin.site.register(Cliente)
admin.site.register(Aluguel)