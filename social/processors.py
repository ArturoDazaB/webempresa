#IMPORTAMOS LA CLASE MODELO "Link"
from .models import Link

#DEFINIMOS LA FUNCION "CONTEXT DICTIONARY" (DICCIONARIO DE CONTEXTO)
def ctx_dict(request):
    #CREAMOS E INICIAMIZAMOS UN NUEVO DICCIONARIO
    ctx = {}
    #IMPORTAMOS TODOS LOS LINKS
    links = Link.objects.all()

    #RECOREMOS CADA UNO DE LOS LINKS
    for link in links:
        #CASAMOS DENTRO DEL DICCIONARIO CREADO CADA KEY CON SU URL
        ctx[link.key] = link.url 

    #RETORNAMOS EL DICCIONARIO
    return ctx