# Generated by Django 2.0.13 on 2019-04-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_remove_livro_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]