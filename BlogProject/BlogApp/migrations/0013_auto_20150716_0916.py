# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0012_auto_20150713_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(blank=True)),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=300)),
                ('slug_name', models.SlugField(blank=True)),
                ('profile_pic', models.ImageField(upload_to=b'images/profile', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(to='BlogApp.UserProfile'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
