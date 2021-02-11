# Generated by Django 2.2 on 2021-02-10 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_auto_20210210_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorsk', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
    ]
