# Generated by Django 4.2.3 on 2023-07-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='carga_horaria',
            field=models.IntegerField(default=1),
        ),
    ]
