# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0038_auto_20181106_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsuccesspage',
            name='topic',
            field=models.TextField(choices=[('contact-success-form', 'Contact domestic form success'), ('contact-events-success-form', 'Contact Events form success'), ('contact-dso-success-form', 'Contact Defence and Security Organisation form success'), ('contact-export-advice-success-form', 'Contact exporting from the UK form success'), ('contact-feedback-success-form', 'Contact feedback form success'), ('contact-find-companies-success-form', 'Contact find UK companies form success'), ('contact-international-success-form', 'Contact international form success')], default='contact-success-form', help_text='The slug and CMS page title are inferred from the topic', unique=True),
            preserve_default=False,
        ),
    ]
