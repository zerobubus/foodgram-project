# Generated by Django 2.2 on 2021-01-28 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210128_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='posts.Ingredient'),
        ),
    ]
