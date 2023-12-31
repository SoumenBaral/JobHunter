# Generated by Django 4.2.7 on 2023-12-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0007_author_jobpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skill',
            field=models.ManyToManyField(to='jobApp.skills'),
        ),
    ]
