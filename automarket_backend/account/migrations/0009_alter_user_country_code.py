# Generated by Django 5.0.3 on 2024-04-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country_code',
            field=models.CharField(default='+995', max_length=10),
        ),
    ]
