# Generated by Django 4.0.6 on 2022-08-10 19:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BNDESIntegration', '0020_alter_archivebndesoperacoes_delete_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivebndesoperacoes',
            name='delete_data',
            field=models.DateField(default=datetime.datetime(2022, 8, 10, 16, 28, 38, 993430)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data_search',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 19, 28, 38, 992179, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='validity_day',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 19, 28, 38, 992213, tzinfo=utc)),
        ),
    ]