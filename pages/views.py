from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id):
    #SE UTILIZA LA FUNCION "GET_OBJECT_OR_404" PORQUE SOLO SE DEBE RECIBIR UN OBJETO
    page = get_object_or_404(Page, id = page_id)
    return render(request, 'pages/sample.html', {'page':page})