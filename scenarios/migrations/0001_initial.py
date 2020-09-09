# Generated by Django 2.2.5 on 2020-03-09 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0002_auto_20200306_1056'),
        ('sites', '0002_auto_20200306_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario_name', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Program')),
                ('site_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'ordering': ('scenario_name',),
                'unique_together': {('program_name', 'site_name', 'scenario_name')},
            },
        ),
    ]