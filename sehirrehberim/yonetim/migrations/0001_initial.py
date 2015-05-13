# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kampanya',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('olusturulma', models.DateTimeField(auto_now_add=True)),
                ('firma', models.CharField(max_length=100)),
                ('kategori', models.CharField(max_length=50)),
                ('enlem', models.CharField(max_length=50)),
                ('boylam', models.CharField(max_length=50)),
                ('baslik', models.CharField(default=b'', max_length=100, blank=True)),
                ('icerik', models.TextField()),
                ('onay', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('olusturulma',),
            },
        ),
    ]
