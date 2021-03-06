# Generated by Django 2.2.5 on 2020-03-02 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0013_auto_20200302_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='existinglight',
            name='installation_type',
            field=models.CharField(choices=[('Recessed Plaster', 'Recessed Plaster'), ('Recessed T-Grid', 'Recessed T-Grid'), ('Surface Mount', 'Surface Mount'), ('Suspended', 'Suspended'), ('Wall Mount', 'Wall Mount'), ('Other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ledlight',
            name='fitting_type',
            field=models.CharField(choices=[('Batten', 'Batten'), ('Bulkhead', 'Bulkhead'), ('Downlight', 'Downlight'), ('Decorative', 'Decorative'), ('Floodlight', 'Floodlight'), ('Highbay', 'Highbay'), ('Other', 'Other'), ('Oyster', 'Oyster'), ('Panel', 'Panel'), ('Weatherproof', 'Weatherproof')], max_length=30),
        ),
    ]
