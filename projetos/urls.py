from django.urls import path
from .views import *

urlpatterns = [
    path('projetos/criar', ProjetoCreateView.as_view(), name='projeto-create'),
    path('projetos/listar/', ProjetoListView.as_view(), name='projeto-list'),
     path('projetos/testeCriar', ProjetoTesteCreateView.as_view(), name='projeto-testeCreate'),
    path('projetos/testeListar/', ProjetoTesteListView.as_view(), name='projeto-testeList'),
]


