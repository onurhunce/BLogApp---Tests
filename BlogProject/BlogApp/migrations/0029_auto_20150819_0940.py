# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0028_auto_20150819_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=11, choices=[(b'Music', b'Music'), (b'Sport', b'Sport'), (b'Fashion', b'Fashion'), (b'Travel', b'Travel'), (b'Cinema', b'Cinema'), (b'Photography', b'Photography'), (b'Food', b'Food'), (b'Technology', b'Technology'), (b'Health', b'Health'), (b'Education', b'Education'), (b'Politics', b'Politics'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
