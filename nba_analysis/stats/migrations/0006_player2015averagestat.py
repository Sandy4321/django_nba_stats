# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_average2015statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player2015AverageStat',
            fields=[
                ('player_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('games_played', models.IntegerField(null=True, blank=True)),
                ('min', models.FloatField(null=True, blank=True)),
                ('fgm', models.FloatField(null=True, blank=True)),
                ('fga', models.FloatField(null=True, blank=True)),
                ('fg_pct', models.FloatField(null=True, blank=True)),
                ('fg3m', models.FloatField(null=True, blank=True)),
                ('fg3a', models.FloatField(null=True, blank=True)),
                ('fg3_pct', models.FloatField(null=True, blank=True)),
                ('ftm', models.FloatField(null=True, blank=True)),
                ('fta', models.FloatField(null=True, blank=True)),
                ('ft_pct', models.FloatField(null=True, blank=True)),
                ('oreb', models.FloatField(null=True, blank=True)),
                ('dreb', models.FloatField(null=True, blank=True)),
                ('reb', models.FloatField(null=True, blank=True)),
                ('ast', models.FloatField(null=True, blank=True)),
                ('stl', models.FloatField(null=True, blank=True)),
                ('blk', models.FloatField(null=True, blank=True)),
                ('tov', models.FloatField(null=True, blank=True)),
                ('foul', models.FloatField(null=True, blank=True)),
                ('pts', models.FloatField(null=True, blank=True)),
                ('plus_minus', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'avg_2015',
                'managed': False,
            },
        ),
    ]
