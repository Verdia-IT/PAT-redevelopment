# Generated by Django 2.2.5 on 2020-03-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0012_existinglight_led_light'),
    ]

    operations = [
        migrations.AlterField(
            model_name='existinglight',
            name='fitting_type',
            field=models.CharField(choices=[('Batten', 'Batten'), ('Bulkhead', 'Bulkhead'), ('Downlight', 'Downlight'), ('Decorative', 'Decorative'), ('Emergency Batten', 'Emergency Batten'), ('Floodlight', 'Floodlight'), ('Highbay', 'Highbay'), ('Other', 'Other'), ('Oyster', 'Oyster'), ('Troffer', 'Troffer'), ('Panel', 'Panel'), ('Weatherproof', 'Weatherproof')], max_length=30),
        ),
    ]
