from .models import *
from django import forms
from django.forms import ModelForm

class fotos(ModelForm):
    class Meta:
        model = Belleza
        fields = ('foto1','foto2','foto3','foto4','foto5')