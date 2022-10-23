from dataclasses import fields
from django import forms
from .models import *

class PostulanteForm(forms.ModelForm):

    class Meta:
        model = Postulante
        fields = '__all__'

class IdiomaForm(forms.ModelForm):

    
    class Meta:
        model = Idioma
        fields = '__all__'



