# Generated by Django 2.2 on 2021-02-10 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0041_auto_20210210_1818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('-created',), 'verbose_name': 'Подписки'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ('-created',), 'verbose_name': 'Покупки'},
        ),
        migrations.AddField(
            model_name='follow',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
