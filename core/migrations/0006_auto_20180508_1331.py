# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-08 09:58
from __future__ import unicode_literals

from modeltranslation.utils import build_localized_fieldname

from django.conf import settings
from django.core.management import call_command
from django.db import migrations


def set_url_path(apps, schema_manager):
    # We cannot use `apps.get_model` because the historic model will not be
    # "patched" by wagtail-modeltranslation, so localized fields
    # will not exist on the historic model - so django will reject updating
    # url_path_en_gb etc because the fields don't exist on the historic model.
    # Impact of using non-historic model should be zero because url_path
    # has always existed on the Page model, so we cannot go to a historic state
    # where url_path is not present on the model: https://goo.gl/CkrUvU

    call_command('sync_page_translation_fields', '--noinput')
    from wagtail.core.models import Page
    url_path = '/'
    field_names = (
        build_localized_fieldname('url_path', code)
        for code, _ in settings.LANGUAGES
    )
    localized_values = {field_name: url_path for field_name in field_names}

    # Avoid calling `save` on each instance so wagtail-modeltranslations does
    # not regenerate the url_path of descendant and ancestor pages, which would
    # fail because some descendants or ancestors have `url_path` set to None
    Page.objects.filter(url_path__isnull=True).update(
        url_path=url_path, **localized_values
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180423_1803'),
    ]

    operations = [
        migrations.RunPython(set_url_path, migrations.RunPython.noop)
    ]
