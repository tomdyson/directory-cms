# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-23 16:19
from __future__ import unicode_literals

from django.db import migrations


def set_historic_slugs(apps, schema_manager):
    Page = apps.get_model('wagtailcore', 'Page')
    HistoricSlug = apps.get_model('core', 'HistoricSlug')

    for model_class in Page.__subclasses__():
        historic_model_class = apps.get_model(
            model_class._meta.app_label,
            model_class._meta.model_name
        )
        for page in historic_model_class.objects.all():
            HistoricSlug.objects.create(
                page=page,
                slug=page.slug
            )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180423_1122'),
    ]

    operations = [
        migrations.RunPython(
            set_historic_slugs,
            migrations.RunPython.noop,
            elidable=True
        )
    ]

