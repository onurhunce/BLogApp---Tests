# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0015_auto_20150723_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_mail',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
