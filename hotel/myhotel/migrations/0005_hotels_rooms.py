# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhotel', '0004_auto_20150102_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100, choices=[(b'Bangalore', b'Bangalore'), (b'Delhi', b'Delhi'), (b'Mumbai', b'Mumbai'), (b'Kolkata', b'Kolkata'), (b'Chennai', b'Chennai')])),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
                ('photo', models.ImageField(upload_to=b'hotelpics', blank=True)),
                ('website', models.URLField(blank=True)),
                ('no_of_rooms', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_checkin', models.DateTimeField()),
                ('date_checkout', models.DateTimeField()),
                ('hotel', models.ForeignKey(to='myhotel.Hotels')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
