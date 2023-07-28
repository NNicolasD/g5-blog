from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"
        
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electrónico',
            'mensaje': 'Mensaje'
        }
        
        widgets = {
            'nombre' : forms.TextInput(attrs= {'class' : 'form-control','placeholder': 'Juan Perez','required': True}),
            'correo' : forms.EmailInput(attrs= {'class' : 'form-control','placeholder': 'juanperez@mail.com','required': True}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control','rows': 5,'required': True})
        }

        message = forms.CharField(
            label="Mensaje",
            widget=forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'required': True,
            })
        )