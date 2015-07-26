# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_avg2015_gamelog2015'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='avg2015',
            table='2014-15 Regular Season Standard Statistics',
        ),
    ]
