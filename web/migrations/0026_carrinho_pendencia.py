# Generated by Django 2.0.13 on 2019-06-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_auto_20190625_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='pendencia',
            field=models.BooleanField(default=True),
        ),
    ]