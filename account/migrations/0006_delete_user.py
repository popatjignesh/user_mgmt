# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180125_0959'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
