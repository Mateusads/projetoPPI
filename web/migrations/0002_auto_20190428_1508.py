# Generated by Django 2.0.13 on 2019-04-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='nome',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='livro',
            name='titulo',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='livro',
            name='sinopse',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='livro',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
