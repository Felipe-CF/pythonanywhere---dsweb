import re
from bazar.forms import *
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


class BazarIndex(View):

    def get(self, request, *args, **kwargs):

        cliente = None

        if request.user.is_authenticated:
             
             cliente = Cliente.objects.get(user=request.user)

        return render(request, 'bazar_index.html', context={'cliente': cliente})
   

class CadastroView(View):

    def get(self, request,*args, **kwargs):

        form = ClienteForm()

        return render(request, "cadastro.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        
        form = ClienteForm(request.POST)

        if form.is_valid():

            login = form.cleaned_data['login']

            senha = form.cleaned_data['senha']

            user = User.objects.create_user(username=login, password=senha)

            cliente = form.save(commit=False)

            cliente.user = user

            cliente.save()

            return HttpResponseRedirect(reverse('bazar:login'))
        
        else:
            form = ClienteForm()

            return render(request, "cadastro.html", {'form': form}) 


class LogarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        dados_requisicao = request.POST

        if dados_requisicao['login'] != '' and  dados_requisicao['senha'] != '':
            nome_login = dados_requisicao.get('login')

            senha = dados_requisicao.get('senha')

            usuario = authenticate(username=nome_login, password=senha)

            if usuario is not None:
                login(request, usuario)

                return redirect(reverse('bazar:bazar_index'))
            
            else:
                messages.error(request, 'O usuario não existe.')

                return render(request, 'login.html')
            
        else:
            messages.error(request, 'Insira os dados obrigatorios.')

            return render(request, 'login.html')


class LogoutView(View):
        
        @method_decorator(login_required)
        def post(self, request, *args, **kwargs):

            logout(request)

            return HttpResponseRedirect(reverse('bazar:bazar_index'))
        

class EditarPerfilView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:

            form = ClienteForm()

            return render(request, "editar.html", context={'form':form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated :

            form = ClienteForm(request.POST)

            if form.is_valid():

                usuario = request.user
                
                nome = form.cleaned_data['nome']

                nome_login = form.cleaned_data['login']
                
                senha = form.cleaned_data['senha']

                cliente = Cliente.objects.get(user=usuario)
                
                if nome is not '' and nome is not None:
                    cliente.nome = nome

                if nome_login is not '' and nome_login is not None:

                    cliente.user.username = nome_login

                    cliente.login = nome_login
                
                if senha is not '' and senha is not None:

                    cliente.senha = senha

                    cliente.user.set_password(senha) 

                cliente.user.save() 

                cliente.save()

                update_session_auth_hash(request, cliente.user)

                return HttpResponseRedirect(reverse('bazar:bazar_index'))
            
            else:
                return HttpResponseRedirect(reverse('bazar:editar'))
                     
        
class DeletePerfilView(View):
        
        @method_decorator(login_required)
        def get(self, request, *args, **kwargs):

            if request.user.is_authenticated:

                usuario_nome = request.user.username

                usuario_removido = User.objects.get(username=usuario_nome)

                usuario_removido.delete()

                return HttpResponseRedirect(reverse('dama:index'))
            
            else:
                messages.error(request, 'Não foi possível deletar a conta')

                return render(request, "perfil.html")
 

class ItemView(View):
        
        @method_decorator(login_required)
        def get(self, request, *args, **kwargs): 

            item = ItemForm()

            return render(request, "item.html", context={'item': item})
        
        @method_decorator(login_required)
        def post(self, request, *args, **kwargs):

            form = ItemForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                return HttpResponseRedirect(reverse('bazar:bazar_index'))
            
            else:

                print(form.errors)

                form_item = ItemForm()

                return render(request, 'item.html', context={'item': form_item})
            

class EventoView(View):
        
        @method_decorator(login_required)
        def get(self, request, *args, **kwargs): 

            form = EventoForm()

            return render(request, "evento.html", context={'form': form})
        
        @method_decorator(login_required)
        def post(self, request, *args, **kwargs):

            form = EventoForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                return HttpResponseRedirect(reverse('bazar:bazar_index'))
            
            else:

                print(form.errors)

                form = EventoForm()

                return render(request, 'item.html', context={'form': form})
                


    










