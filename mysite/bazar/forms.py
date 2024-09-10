from bazar.models import *
from django import forms

class ClienteForm(forms.ModelForm):


    class Meta:
        model = Cliente

        fields = ['nome', 'login', 'senha']
        
        widgets = {
            'senha': forms.PasswordInput()
        }