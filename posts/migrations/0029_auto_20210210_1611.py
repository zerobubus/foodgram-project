# Generated by Django 2.2 on 2021-02-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.PositiveIntegerField(verbose_name='время'),
        ),
    ]
