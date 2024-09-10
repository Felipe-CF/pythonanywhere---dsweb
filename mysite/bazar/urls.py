from . import views
from django.urls import path


# namespace
app_name = 'bazar'

urlpatterns = [
    path('', views.BazarIndex.as_view(), name='bazar_index'),
    path('login/', views.LogarView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('editar/', views.EditarPerfilView.as_view(), name='editar'),
]


