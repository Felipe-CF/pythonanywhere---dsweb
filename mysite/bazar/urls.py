from . import views
from django.urls import path


# namespace
app_name = 'bazar'

urlpatterns = [
    path('', views.BazarIndex.as_view(), name='bazar_index'),
]


