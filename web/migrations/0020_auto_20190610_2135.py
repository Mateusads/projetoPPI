# Generated by Django 2.0.13 on 2019-06-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20190429_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.CharField(choices=[('1', 'Ação'), ('2', 'Aventura'), ('3', 'Crônica'), ('4', 'Drama'), ('5', 'Ficcao'), ('6', 'Infantil'), ('7 ', 'Poesia '), ('8', 'Romance')], max_length=100),
        ),
    ]
