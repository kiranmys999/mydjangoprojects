# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhotel', '0006_auto_20150105_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkin_date', models.DateTimeField()),
                ('checkout_date', models.DateTimeField()),
                ('hotel', models.ForeignKey(to='myhotel.Hotel')),
                ('room', models.ForeignKey(to='myhotel.Room')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='room',
            name='date_checkin',
        ),
        migrations.RemoveField(
            model_name='room',
            name='date_checkout',
        ),
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
        migrations.AddField(
            model_name='room',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.CharField(default=b'Double', max_length=10, choices=[(b'Single', b'Single'), (b'Double', b'Double')]),
            preserve_default=True,
        ),
    ]
