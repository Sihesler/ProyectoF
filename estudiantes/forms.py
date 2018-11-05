from django import forms
from .models import Curso, Estudiante


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'materia',
            'profesor',
            'hora',
            'estudiantes',
        ]
        def __init__ (self, *args, **kwargs):
            super(CursoForm, self).__init__(*args, **kwargs)
            #En este caso vamos a usar el widget checkbox multiseleccionable.
            self.fields["estudiantes"].widget = forms.widgets.CheckboxSelectMultiple()
            #Podemos usar un texto de ayuda en el widget
            self.fields["estudiantes"].help_text = "Ingrese los Estudiantes que recibiran el Curso"
            #En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
            self.fields["estudiantes"].queryset = Estudiante.objects.all()

        #labels = {
        #    'materia'     : 'Materia',
        #    'profesor'   : 'Profesor',
        #    'hora'       : 'Hora',
        #    'estudiantes': 'Estudiantes',
        #}

        #widgets = {
        #    'materia'     : forms.TextInput(attrs={'class':'form-control'}),
        #    'profesor'    : forms.TextInput(attrs={'class':'form-control'}),
        #    'hora'        : forms.TextInput(attrs={'class':'form-control'}),
        #    'estudiantes' : forms.CheckboxSelectMultiple(),
        #}
