# Generated by Django 2.2 on 2021-01-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210127_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(to='posts.Ingredient'),
        ),
    ]