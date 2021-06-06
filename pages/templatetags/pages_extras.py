# IMPORTAMOS EL MODULO DE REGISTRO DE TEMPLATES
from django import template
# IMPORTAMOS LOS MODELOS
from pages.models import Page

# IMPORTAMOS LA LIBRERIA DE TEMPLATES
register = template.Library() 

@register.simple_tag    # => TRANSFORMA UNA FUNCION EN UN TAG SIMPLE Y LO REGISTRAMOS EN LA LIBRERIA DE TEMPLATES DE DJANGO
def get_page_list():
    pages = Page.objects.all()
    return pages