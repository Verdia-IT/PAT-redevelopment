# Generated by Django 2.2.5 on 2020-03-12 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0001_initial'),
        ('powerbillinputs', '0002_demandcharge'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff_name', models.CharField(max_length=15)),
                ('include', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('frequency', models.CharField(choices=[('Daily', 'Daily'), ('Monthly', 'Monthly')], max_length=15)),
                ('category', models.CharField(choices=[('Retail', 'Retail'), ('Network', 'Network'), ('Marketing', 'Marketing'), ('Environmental', 'Environmental'), ('Metering', 'Metering'), ('Others', 'Others')], max_length=10)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenarios.Scenario')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
