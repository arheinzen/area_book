# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseHold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=1)),
                ('family_role', models.CharField(blank=True, max_length=15)),
                ('member_status', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='LastName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.HouseHold')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_body', models.TextField()),
                ('date_posted', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='individual',
            name='last_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.LastName'),
        ),
        migrations.AddField(
            model_name='individual',
            name='notes_body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Notes'),
        ),
    ]
