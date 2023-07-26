# Generated by Django 4.2.1 on 2023-07-26 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("financas", "0009_usuario_apelido"),
    ]

    operations = [
        migrations.AddField(
            model_name="balancete",
            name="usuario",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="financas.usuario",
            ),
        ),
        migrations.AddField(
            model_name="usuario",
            name="usuario",
            field=models.OneToOneField(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="lancamento",
            name="foto",
            field=models.ImageField(
                default="/../mysite/media/img/financas/DiagramaDominioFinancas.png",
                upload_to="mysite/media/img/financas/",
            ),
        ),
    ]