# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=25)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=140)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('caption', models.TextField(max_length=140)),
                ('active', models.BooleanField(default=True)),
                ('collection', models.ForeignKey(to='dbapi.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('body', models.TextField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=140)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(to='dbapi.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=500)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='dbapi.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=140)),
                ('active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(to='dbapi.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=75)),
                ('description', models.TextField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=140)),
                ('active', models.BooleanField(default=True)),
                ('team', models.ForeignKey(to='dbapi.Team')),
            ],
        ),
    ]
