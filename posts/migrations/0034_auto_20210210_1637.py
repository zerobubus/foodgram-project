# Generated by Django 2.2 on 2021-02-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20210210_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата публикации'),
        ),
    ]
