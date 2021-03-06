# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0010_performancedashboardnotespage'),
    ]

    operations = [
        migrations.AddField(
            model_name='getfinancepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancedashboardnotespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancedashboardpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privacyandcookiespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='termsandconditionspage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], default='', max_length=100),
            preserve_default=False,
        ),
    ]
