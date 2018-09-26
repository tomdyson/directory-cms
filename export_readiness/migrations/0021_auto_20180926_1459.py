# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('export_readiness', '0020_articlelistingpage_articlepage_topiclandingpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newgetfinancepage',
            name='evidence_video_embed',
        ),
        migrations.AddField(
            model_name='newgetfinancepage',
            name='evidence_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
    ]
