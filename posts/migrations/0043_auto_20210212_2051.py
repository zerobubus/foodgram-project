# Generated by Django 2.2 on 2021-02-12 20:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0042_auto_20210210_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]