# Generated by Django 2.2.5 on 2020-06-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0003_auto_20200318_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
