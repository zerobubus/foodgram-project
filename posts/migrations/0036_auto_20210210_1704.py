# Generated by Django 2.2 on 2021-02-10 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_auto_20210210_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Рецепт'},
        ),
    ]
