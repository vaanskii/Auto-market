# Generated by Django 5.0.3 on 2024-04-21 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_image_for_car', to='cars.imagemodel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='airbags',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='cylinders',
            field=models.CharField(blank=True, choices=[('4', '4'), ('6', '6'), ('8', '8'), ('10', '10'), ('12', '12')], default='8', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(blank=True, choices=[('2', '2'), ('4', '4'), ('5', '5'), ('More', 'More')], default='4', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='images',
            field=models.ManyToManyField(blank=True, to='cars.imagemodel'),
        ),
    ]