from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CursoForm, EstudianteForm
from estudiantes.models import Estudiante, Curso
from django.contrib import messages


def index(request):
    return render(request, 'estudiante/index.html')


def estudiante_list(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'estudiante/listar_estudiante.html', {'estudiantes':estudiante})


def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'estudiante/listar_cursos.html', {'cursos':curso})



def curso_nuevo(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            #curso = Curso.objects.Create(materia=formulario.cleaned_data['materia'], profesor=formulario.cleaned_data['profesor'], hora=formulario.cleaned_data['hora'])
            curso = Curso.objects.create(materia=formulario.cleaned_data['materia'], profesor=formulario.cleaned_data['profesor'], hora=formulario.cleaned_data['hora'])
            for estudiante_id in request.POST.getlist('estudiantes'):
                asignacion = Asignacion(estudiante_id=estudiante_id, curso_id = curso.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'estudiante/curso_nuevo.html', {'formulario': formulario})
