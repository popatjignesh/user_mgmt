# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180125_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'abc@xyz.com', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=b'xyz', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'abc', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=b'abc', max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=b'abc', max_length=25),
        ),
    ]
