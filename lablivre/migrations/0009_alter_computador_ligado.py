# Generated by Django 4.2.3 on 2023-08-08 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lablivre', '0008_alter_computador_options_alter_laboratorio_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computador',
            name='ligado',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='ligado'),
        ),
    ]
