# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Gender', models.BooleanField(default=False)),
                ('Age', models.IntegerField(default=19)),
                ('memo', models.TextField(default=b'tomxxx')),
                ('CreatDate', models.DateTimeField(default=b'2015-08-08 08:08:08')),
            ],
        ),
    ]
