# Generated by Django 2.2 on 2021-01-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210128_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='amount',
        ),
        migrations.AddField(
            model_name='recipe',
            name='amount',
            field=models.ManyToManyField(to='posts.Amount'),
        ),
    ]