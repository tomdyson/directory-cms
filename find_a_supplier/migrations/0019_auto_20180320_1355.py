# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 13:55
from __future__ import unicode_literals

from wagtail.core.fields import RichTextField

from django.db import migrations
import find_a_supplier.models


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0018_auto_20180316_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_ar',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_de',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_en_gb',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_es',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_fr',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_ja',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_pt',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_pt_br',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_ru',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industryarticlepage',
            name='body_zh_hans',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_ar',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_de',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_en_gb',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_es',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_fr',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_ja',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_pt',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_pt_br',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_ru',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='hero_text_zh_hans',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_ar',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_ar',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_de',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_en_gb',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_es',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_fr',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_ja',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_pt',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_pt_br',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_ru',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_one_zh_hans',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_ar',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_de',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_en_gb',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_es',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_fr',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_ja',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_pt',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_pt_br',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_ru',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_three_zh_hans',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_ar',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_de',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_en_gb',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_es',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_fr',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_ja',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_pt',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_pt_br',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_ru',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_column_two_zh_hans',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_de',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_en_gb',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_es',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_fr',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_ja',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_pt',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_pt_br',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_ru',
            field=RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='industrypage',
            name='lede_zh_hans',
            field=RichTextField(null=True),
        ),
    ]
