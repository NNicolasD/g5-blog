from django import forms
from .models import Articulo, Comentario
from ckeditor.widgets import CKEditorWidget

class CrearArticuloForm(forms.ModelForm):    
    contenido = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Articulo
        fields = '__all__'
        exclude = ('autor', 'etiqueta',)
        
        widgets = {
            'titulo' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'bajada' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categoria' : forms.Select(attrs={'class' : 'form-select'}),
        }
        
class CrearComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        
        labels = {
            'texto': ''
        }
        
        widgets = {
            'texto' : forms.TextInput(attrs= {'class' : 'form-control', 'placeholder' : 'Escribe un comentario'})
        }