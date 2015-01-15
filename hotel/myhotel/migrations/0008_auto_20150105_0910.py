# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhotel', '0007_auto_20150105_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='no_of_rooms',
        ),
        migrations.AddField(
            model_name='reservation',
            name='no_of_rooms',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.BooleanField(default=False, verbose_name=b'Booked?'),
            preserve_default=True,
        ),
    ]
