# Generated by Django 2.2.5 on 2020-03-31 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarpfc', '0007_pfcprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfcprice',
            name='system_unit_cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
