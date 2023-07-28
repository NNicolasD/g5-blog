from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }