# Generated by Django 3.2.2 on 2021-05-31 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
