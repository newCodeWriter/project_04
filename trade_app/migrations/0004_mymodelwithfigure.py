# Generated by Django 3.1.1 on 2020-10-03 00:48

from django.db import migrations, models
import django_matplotlib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trade_app', '0003_auto_20200929_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelWithFigure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fig', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
    ]
