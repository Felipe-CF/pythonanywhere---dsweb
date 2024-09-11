from bazar.models import *
from django import forms

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = ['nome', 'login', 'senha']
        
        widgets = {
            'senha': forms.PasswordInput()
        }

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item

        fields = ['titulo', 'descricao', 'preco', 'foto']
        
    def __init__(self, *args, **kwargs):

        super(ItemForm, self).__init__(*args, **kwargs)

        self.fields['preco'].initial = 0  