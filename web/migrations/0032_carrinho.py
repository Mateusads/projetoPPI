# Generated by Django 2.0.13 on 2019-06-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_auto_20190625_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Espera', max_length=50)),
                ('livro', models.ManyToManyField(related_name='livros', to='web.Livro')),
            ],
        ),
    ]
