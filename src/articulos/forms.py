from django import forms
from .models import Articulo, Comentario, Categoria
from ckeditor.widgets import CKEditorWidget

class CrearArticuloForm(forms.ModelForm):    
    contenido = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Articulo
        fields = '__all__'
        exclude = ('autor', 'etiqueta', 'publicado')
        
        widgets = {
            'titulo' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'bajada' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
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
        
        
class EditarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        exclude = ['user_id']

        
        labels = {
            'texto': ''
        }
        
class CrearCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        
        
        widgets = {
            'texto' : forms.TextInput(attrs= {'class' : 'form-control'})
        }