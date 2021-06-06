from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
class Category(models.Model):
    name = CharField(max_length=100, verbose_name='Nombre')
    created = DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name

from django.utils.timezone import now
from django.contrib.auth.models import User

class Post(models.Model):
    title = CharField(max_length=200, verbose_name='Título')
    content = TextField(verbose_name='Contenido')
    published = DateTimeField(verbose_name='Fecha de Publicación', default=now)
    image = ImageField(verbose_name='Imagen', upload_to = 'blog', null = True, blank = True)
    author = ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = ManyToManyField(Category, verbose_name='Categorias', related_name='get_post')
    created = DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title    