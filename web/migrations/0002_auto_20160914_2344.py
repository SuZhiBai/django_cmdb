# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Age',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='CreatDate',
            field=models.DateTimeField(default=b'2015-08-08 08:08'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(default=1, to='web.UserType'),
        ),
    ]
