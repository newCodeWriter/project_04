# Generated by Django 3.1.1 on 2020-10-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_app', '0010_auto_20201004_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cash_balance',
            field=models.DecimalField(decimal_places=2, default=1500.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='stockorder',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
