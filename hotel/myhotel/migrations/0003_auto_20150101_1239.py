# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhotel', '0002_auto_20141229_1051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoginForm',
            new_name='Login',
        ),
    ]
