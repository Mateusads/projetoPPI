import datetime
from django.db import models
from django.utils import  timezone


# Create your models here.
class Livro(models.Model):

    titulo = models.CharField(max_length = 50, default="")
    autor = models.CharField(max_length=50, default="")
    ano = models.DateTimeField('ano de publicacao')

    BOOK_CHOICES = (
        ('Drama', 'Drama'),
        ('Ficcao', 'Ficcao'),
        ('Ação', 'Ação'),
        ('Romance', 'Romance'),
        ('Cronica', 'Crônica' ),
        ('Poesia ', 'Poesia '),
        ('Aventura', 'Aventura'),  
        ('Infantil', 'Infantil'),


    )
    genero = models.CharField(max_length = 100, choices = BOOK_CHOICES)
    
    sinopse = models.CharField(max_length = 2000)
    valor = models.FloatField(default=0)
    venda = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='media/pictures/%Y/%m/%d/',max_length=255, null=True, blank=True)

    def salvar(self):
        self.save()

    def getSinopse(self):
        return self.sinopse


    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=50)
    email = models.EmailField(blank=True, default="")


    def salvar(self):
        self.save()

    def getCpf(self):
        return self.cpf

    def __str__(self):
        return self.nome

class Rent(models.Model):
    BOOK_CHOICES = (
        ('Alugar', 'Alugar'),
        ('Comprar', 'Comprar'),
    )
    tipo = models.CharField(max_length = 50, choices = BOOK_CHOICES)
    observacao = models.CharField(max_length = 50, default="")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_rent = models.DateField(default=timezone.now())
    data_devolucao = models.DateField(default=timezone.now())

    def salvar(self):
        self.save()

    def __str__(self):
        return self.tipo
