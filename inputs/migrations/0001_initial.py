# Generated by Django 2.2.5 on 2020-03-10 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scenarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bills', models.IntegerField()),
                ('bill_month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10)),
                ('bill_year', models.IntegerField()),
                ('bill_days', models.IntegerField()),
                ('electricity_retailer', models.CharField(choices=[('1st energy', '1st energy'), ('ActewAGL', 'ActewAGL'), ('AGL Energy', 'AGL Energy'), ('Alinta Energy ', 'Alinta Energy '), ('Aurora Energy ', 'Aurora Energy '), ('Blue NRG', 'Blue NRG'), ('Click Energy ', 'Click Energy '), ('Commander', 'Commander'), ('Cova U', 'Cova U'), ('Dodo Power & Gas ', 'Dodo Power & Gas '), ('Diamond Energy ', 'Diamond Energy '), ('EnergyAustralia ', 'EnergyAustralia '), ('Ergon Energy ', 'Ergon Energy '), ('ERM Business Energy\xa0', 'ERM Business Energy\xa0'), ('GloBird Energy', 'GloBird Energy'), ('Horizon Power', 'Horizon Power'), ('Lumo Energy', 'Lumo Energy'), ('Momentum Energy ', 'Momentum Energy '), ('Next Business Energy', 'Next Business Energy'), ('Origin Energy ', 'Origin Energy '), ('Pacific Hydro', 'Pacific Hydro'), ('People Energy', 'People Energy'), ('Perth Energy', 'Perth Energy'), ('Powerdirect', 'Powerdirect'), ('Powershop', 'Powershop'), ('Qenergy', 'Qenergy'), ('Red Energy ', 'Red Energy '), ('Sanctuary Energy', 'Sanctuary Energy'), ('Simply Energy ', 'Simply Energy '), ('Sumo Power', 'Sumo Power'), ('Synergy', 'Synergy'), ('Urth Energy', 'Urth Energy'), ('WinEnergy', 'WinEnergy'), ('Other', 'Other')], max_length=30)),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scenarios.Scenario')),
            ],
        ),
    ]