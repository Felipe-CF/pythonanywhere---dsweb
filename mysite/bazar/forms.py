from bazar.models import *
from django import forms
from django.forms import DateTimeInput

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


class EventoForm(forms.ModelForm):

    itens = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.SelectMultiple,  # Ou SelectMultiple, dependendo da interface
        required=False
    )

    class Meta:
        model = Evento

        fields = ['nome', 'banner', 'data_inicio', 'data_fim', 'itens']

        widgets ={
            'data_inicio': DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_fim': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        



