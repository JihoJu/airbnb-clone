# Generated by Django 2.2.5 on 2021-07-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20210706_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='created',
            field=models.DateField(default=''),
        ),
    ]