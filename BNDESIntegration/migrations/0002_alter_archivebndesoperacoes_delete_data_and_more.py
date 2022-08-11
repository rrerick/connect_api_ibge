# Generated by Django 4.0.6 on 2022-08-10 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BNDESIntegration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivebndesoperacoes',
            name='delete_data',
            field=models.DateField(default=datetime.datetime(2022, 8, 10, 12, 9, 10, 414004)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data_search',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 15, 9, 10, 413065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='validity_day',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 15, 9, 10, 413092, tzinfo=utc)),
        ),
    ]