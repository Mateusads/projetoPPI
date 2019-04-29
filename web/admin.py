from django.contrib import admin
from .models import Livro, Cliente, Rent

# Register your models here.

admin.site.register(Livro)
admin.site.register(Cliente)
admin.site.register(Rent)