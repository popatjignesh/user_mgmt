# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_cnfrm_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='cnfrm_password',
            new_name='confirm_password',
        ),
    ]
