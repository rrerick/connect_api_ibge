# Generated by Django 4.0.6 on 2022-08-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_operacoes_delete_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacoes',
            name='delete_time',
            field=models.DateTimeField(),
        ),
    ]
