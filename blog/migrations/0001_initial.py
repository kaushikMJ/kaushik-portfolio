# Generated by Django 4.0.5 on 2022-07-31 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
