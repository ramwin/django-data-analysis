# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('food', 'food'), ('drink', 'drink')], max_length=31)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=1)),
                ('total_price', models.IntegerField(default=1)),
                ('amount', models.IntegerField(default=1)),
            ],
        ),
    ]
