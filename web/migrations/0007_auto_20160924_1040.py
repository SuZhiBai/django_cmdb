# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20160924_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usenmae',
            new_name='usernmae',
        ),
    ]
