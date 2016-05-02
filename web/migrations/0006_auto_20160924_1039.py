# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='usenmae',
        ),
    ]
