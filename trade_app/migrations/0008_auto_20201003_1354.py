# Generated by Django 3.1.1 on 2020-10-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_app', '0007_auto_20201003_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockorder',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='stockorder',
            name='stock',
        ),
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='StockOrder',
        ),
    ]
