# Generated by Django 4.2.7 on 2023-12-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0003_jobpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]