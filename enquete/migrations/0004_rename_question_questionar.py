# Generated by Django 4.0.6 on 2023-04-20 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0003_rename_question_choice_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='question',
            new_name='Questionar',
        ),
    ]
