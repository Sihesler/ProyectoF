from django.conf.urls import url
from . import views
from estudiantes.views import index, curso_list

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^lista$', views.index, name='index'),
    url(r'^lista/nuevo$', views.curso_nuevo, name='curso_nuevo'),
    url(r'^listar$', views.curso_list, name='curso_list'),
]
