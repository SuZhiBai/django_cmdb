# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20161002_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostroom',
            name='id',
        ),
        migrations.AddField(
            model_name='hostroom',
            name='hostroomid',
            field=models.AutoField(default=1000, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
