# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_auto_20150708_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=11, choices=[(b'MSC', b'Music'), (b'SP', b'Sport'), (b'FAS', b'Fashion'), (b'TRV', b'Travel'), (b'CIN', b'Cinema'), (b'PHO', b'Photography'), (b'FO', b'Food'), (b'TECH', b'Technology'), (b'HEALTH', b'Health'), (b'EDU', b'Education'), (b'POL', b'Politics'), (b'OTH', b'Other')]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(max_length=2000),
        ),
    ]
