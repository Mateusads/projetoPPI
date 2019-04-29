# Generated by Django 2.0.13 on 2019-04-29 00:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20190428_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.CharField(choices=[('Drama', 'Drama'), ('Ficcao', 'Ficcao'), ('Acao', 'Acao'), ('Romance', 'Romance'), ('Cronica', 'Crônica'), ('Poesia ', 'Poesia '), ('Aventura', 'Aventura')], max_length=100),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_devolucao',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 0, 3, 43, 29153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_rent',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 0, 3, 43, 29124, tzinfo=utc)),
        ),
    ]
