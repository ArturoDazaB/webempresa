from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Service(models.Model):
    title = CharField(max_length=200, verbose_name='Titulo')
    subtitle = CharField(max_length=200, verbose_name='Subtitulo')
    content = TextField(verbose_name='Contenido') 
    image = ImageField(verbose_name='Imagen', upload_to = 'services')
    created = DateTimeField(auto_now_add='true', verbose_name='Fecha de Creacion')
    updated = DateTimeField(auto_now='true', verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title