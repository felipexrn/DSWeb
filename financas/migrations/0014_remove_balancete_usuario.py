# Generated by Django 4.2.1 on 2023-07-26 12:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("financas", "0013_alter_usuario_usuario"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="balancete",
            name="usuario",
        ),
    ]