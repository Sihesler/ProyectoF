# Generated by Django 2.1.3 on 2018-11-04 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nombre',
            new_name='materia',
        ),
    ]
