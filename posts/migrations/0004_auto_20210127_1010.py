# Generated by Django 2.2 on 2021-01-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210127_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(blank=True, null=True, related_name='recipes', to='posts.Ingredient', verbose_name='ingredient'),
        ),
    ]
