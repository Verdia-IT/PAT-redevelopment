# Generated by Django 2.2.5 on 2020-08-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_programoverride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programoverride',
            name='cashflow_start_month',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)]),
        ),
    ]