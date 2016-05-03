# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20160925_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostroom',
            old_name='Name',
            new_name='contacts',
        ),
        migrations.AddField(
            model_name='host',
            name='equmodel',
            field=models.CharField(default='dell', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='hostroom',
            field=models.ForeignKey(default=1, to='web.HostRoom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='personin',
            field=models.CharField(default='zhang', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='racknum',
            field=models.CharField(default='E1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostroom',
            name='isp',
            field=models.CharField(default='liantong', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostroom',
            name='roomcity',
            field=models.CharField(default='beijing', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostroom',
            name='roomname',
            field=models.CharField(default='shijihulian', unique=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostroom',
            name='telephone',
            field=models.BigIntegerField(default=13717801234L),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostroom',
            name='tradename',
            field=models.CharField(default='dilian', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.IPAddressField(unique=True),
        ),
    ]
