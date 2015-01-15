# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginform',
            old_name='name',
            new_name='username',
        ),
    ]
