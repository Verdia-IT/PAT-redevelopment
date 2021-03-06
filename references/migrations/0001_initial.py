# Generated by Django 2.2.5 on 2020-02-25 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificatePrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STCprice', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('VEECprice', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('ESCprice', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2019', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2020', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2021', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2022', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2023', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2024', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2025', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2026', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2027', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2028', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2029', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
                ('LGCprice2030', models.DecimalField(decimal_places=2, default=36.0, max_digits=6)),
            ],
        ),
    ]
