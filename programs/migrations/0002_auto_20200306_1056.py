# Generated by Django 2.2.5 on 2020-03-06 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ('program_name',)},
        ),
    ]