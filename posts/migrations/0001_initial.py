# Generated by Django 2.2 on 2021-01-25 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='имя')),
                ('description', models.TextField(verbose_name='описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
