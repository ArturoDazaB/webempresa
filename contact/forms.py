from django import forms

class ContactForm(forms.Form):
    # CAMPO 'Nombre' DEL FORMULARIO "Contacto"
    name = forms.CharField(
        label='Nombre', 
        required=True, 
        #DEFINIMOS LA PROPIEDAD WIDGET DEL CAMPO DE FORMULARIO 'Nombre'
        #NOTA: LA PROPIEDAD WIDGET ES LA REPRESENTACION DE UN ELEMENTO
        #      INPUT HTML PARA DJANGO.
        widget=forms.TextInput(
            #ATRIBUTOS DEL WIDGET
            attrs={
                #EXTENSION DE LA CLASE 'form-control'
                'class':'form-control',
                #MENAJE QUE SE MOSTRARA EN EL INPUT NOMBRE
                'placeholder':'Escribe aqui tu nombre',
            }
        ),
        min_length=3,
        max_length=100,
    )

    # CAMPO 'Email/Correo Electronico' DEL FORMULARIO "Contacto"
    email = forms.EmailField(
        label='Email', 
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Escribe aqui tu correo electronico',
            }
        ),
        min_length=3,
        max_length=100,
    )

    # CAMPO 'Mensaje' DEL FORMULARIO "Contacto"
    content = forms.CharField(
        label='Contenido', 
        required=True, 
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':3,
                'placeholder':'Aqui escribe tu mensaje',
            }
        ),
        min_length=10,
        max_length=100,
    )