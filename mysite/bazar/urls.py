from . import views
from django.urls import path


# namespace
app_name = 'bazar'

urlpatterns = [
    path('', views.BazarIndex.as_view(), name='bazar_index'),
    path('login/', views.LogarView.as_view(), name='login'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
]


