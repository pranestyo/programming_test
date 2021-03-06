# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-10 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('date_published', models.DateField()),
                ('number_of_page', models.IntegerField()),
                ('type_of_book', models.CharField(choices=[('one_of_novel', 'One of Novel'), ('documentation', 'Documentation'), ('other', 'Other')], max_length=20)),
            ],
        ),
    ]
