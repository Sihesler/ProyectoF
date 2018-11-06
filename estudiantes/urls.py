from django.conf.urls import url
from . import views
from estudiantes.views import index, curso_list

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.index, name='index'),
    url(r'^listar_estudiante$', views.estudiante_list, name='estudiante_list'),
    url(r'^listar_curso$', views.curso_list, name='curso_list'),
    url(r'^nuevo$', views.curso_nuevo, name='curso_nuevo'),
    url(r'^nuevo_estudiante$', views.estudiante_nuevo, name='estudiante_nuevo'),

    #url(r'^detalle$', views.curso_detalle, name='curso_detalle'),
    #url(r'^listar$', views.curso_list, name='curso_list'),
]
