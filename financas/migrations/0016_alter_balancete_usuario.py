# Generated by Django 4.2.1 on 2023-07-26 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("financas", "0015_balancete_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="balancete",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="financas.usuario"
            ),
        ),
    ]
