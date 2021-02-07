# Generated by Django 2.2 on 2021-01-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20210128_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(related_name='recipes', through='posts.Amount', to='posts.Ingredient'),
        ),
    ]
