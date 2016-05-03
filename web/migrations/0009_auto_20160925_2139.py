# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20160924_1041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Asset',
            new_name='Host',
        ),
        migrations.RenameModel(
            old_name='Group',
            new_name='HostRoom',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='typeId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='group_relation',
        ),
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.ForeignKey(default=2, to='web.UserType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
