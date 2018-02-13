# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180125_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cnfrm_password',
            field=models.CharField(default=b'abc', max_length=25),
            preserve_default=True,
        ),
    ]
