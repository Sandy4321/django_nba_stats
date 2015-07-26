# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20150721_1831'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='avg2015',
            table='avg_2015',
        ),
    ]
