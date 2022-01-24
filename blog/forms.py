from django import forms
from .models import Post

# Clase para la creacion del post
class PostForm(forms.ModelForm): #En este caso usamos ModelForm porque los campos vienen del modelo
    class Meta:
        model = Post
#        fields = ('title', 'slug', 'autor', 'body')
        fields = ('title', 'autor', 'body')
        
        widgets = {
# Pasamos CSS (la clase) y parametros
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la receta'}), 
#            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Slug'}), 
            'autor': forms.Select(attrs={'class':'form-control'}), 
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Instrucciones'}), 
        }
        
# Clase para la edicion del post
class EditForm(forms.ModelForm): #En este caso usamos ModelForm porque los campos vienen del modelo
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        widgets = {
# Pasamos CSS (la clase) y parametros
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la receta'}), 
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Instrucciones'}), 
        }

