from django.shortcuts import render, redirect
from django.http import HttpResponse
from estudiantes.forms import CursoForm
from estudiantes.models import Curso, Asignacion


def index(request):
    return render(request, 'estudiante/index.html')


def curso_nuevo(request):
    if request.method == 'Post':
        formulario = CursoForm(request.Post)
        if formulario.is_valid():
            formulario.save()
        return redirect('estudiante:index')
    else:
        formulario = CursoForm()
    return render(request, 'estudiante/curso_nuevo.html', {'formulario': formulario})


def curso_list(request):
    curso = Curso.objects.all()
    contexto = {'cursos':curso}
    return render(request, 'estudiante/curso_list.html', contexto)
