# Generated by Django 5.0.6 on 2024-05-23 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('categories', models.ManyToManyField(to='mainapp.category')),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
            ],
            options={
                'db_table': 'attendee',
            },
        ),
    ]