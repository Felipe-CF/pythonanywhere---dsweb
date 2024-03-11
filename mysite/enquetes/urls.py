from . import views
from django.urls import path


urlpatterns = [
    # path('caminho', 'elemento de view', 'nome')
    path('', views.index, name='index'),

]


