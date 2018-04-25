# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-25 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0050_auto_20180425_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industrypagearticlesummary',
            name='industry_name',
            field=models.CharField(blank=True, help_text='Informs the reader of which industry the article is for.', max_length=255),
        ),
        migrations.AlterField(
            model_name='landingpagearticlesummary',
            name='industry_name',
            field=models.CharField(blank=True, help_text='Informs the reader of which industry the article is for.', max_length=255),
        ),
    ]
