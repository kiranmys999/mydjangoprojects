# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhotel', '0005_hotels_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_checkin', models.DateTimeField()),
                ('date_checkout', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='user',
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(to='myhotel.Hotel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
