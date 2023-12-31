# Generated by Django 4.1.5 on 2023-05-05 05:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0002_estudiante_horario_participante_periodoacademico_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='persona_ptr',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='persona_ptr',
        ),
        migrations.RemoveField(
            model_name='rol',
            name='permisos_rol',
        ),
        migrations.AlterModelOptions(
            name='materia',
            options={'verbose_name': 'Materia', 'verbose_name_plural': 'Materias'},
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='fecha_creacion',
            new_name='fecha_creacion_curso',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='fecha_actualizacion',
            new_name='fecha_actualizacion_horarios',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='fecha_creacion',
            new_name='fecha_creacion_horarios',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='rol',
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_actualizacion_curso',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_estudiante', to='AppUsuarios.persona'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_participante', to='AppUsuarios.persona'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsuarios.persona'),
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Participante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
