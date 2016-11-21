# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.User')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('start_date', models.DateTimeField(max_length=255)),
                ('end_date', models.DateTimeField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logreg.User')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Travel'),
        ),
    ]
