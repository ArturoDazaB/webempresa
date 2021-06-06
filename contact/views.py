from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):

    contact_form = ContactForm()

    if(request.method == "POST"):
        contact_form = ContactForm(data=request.POST)

        if(contact_form.is_valid()):
            name = request.POST.get('name', '')
            email =  request.POST.get('email', '')
            content = request.POST.get('content', '')

            # CARGAMOS LA INFORMACION DE CONTACTO PARA ENVIARLA EN UN CORREO NUEVO
            email = EmailMessage(
                "La Caffettiera: Nuevo menaje de contacto", 
                "De {} <{}>\n\nEscribio\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io", 
                ["carlos.arturo.dazab@gmail.com"],
                reply_to=[email], 
            )

            #ENVIAMOS EL CORREO Y REDIRECCIONAMOS A LA PAGINA CONTACT OK
            try:
                # SE IMPRIME EN CONSOLA LA INFORMACION DEL CONTACTO
                print('Nombre del contacto: ', name)
                print('Email del contacto: ', email)
                print('Contenido del mensaje: ', content)
                # SE ENVIA EL CORREO LA DIRECCION PROPORCIONADA PREVIAMENTE
                email.send()
                # TODO A IDO BIEN, REDIRECCIONAMOS A OK
                return redirect(reverse('contact')+"?ok")
            except:
                # ALGO A IDO MAL REDIRECCIONAMOS A FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form':contact_form})