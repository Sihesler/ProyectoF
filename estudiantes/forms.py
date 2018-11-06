from django import forms
from .models import Curso, Estudiante



class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('materia', 'profesor', 'hora', 'estudiantes')

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'edad', 'fecha_nacimiento', 'direccion')



def __init__ (self, *args, **kwargs):
    super(CursoForm, self).__init__(*args, **kwargs)
    #En este caso vamos a usar el widget checkbox multiseleccionable.
    fields.fields["estudiantes"].widget = forms.widgets.CheckboxSelectMultiple()
    #Podemos usar un texto de ayuda en el widget
    fields.fields["estudiantes"].help_text = "Ingrese los Estudiantes que recibiran el Curso"
    #En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
    fields.fields["estudiantes"].queryset = Estudiante.objects.all()
