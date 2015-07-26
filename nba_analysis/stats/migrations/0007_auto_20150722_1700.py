# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_player2015averagestat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player2015averagestat',
            options={'ordering': ['pts', 'last_name'], 'managed': False},
        ),
    ]
