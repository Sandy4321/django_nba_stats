# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avg2015',
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
        migrations.CreateModel(
            name='GameLog2015',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season_id', models.IntegerField(null=True, blank=True)),
                ('player_id', models.IntegerField(null=True, blank=True)),
                ('game_id', models.IntegerField(null=True, blank=True)),
                ('game_month', models.CharField(max_length=10, null=True, blank=True)),
                ('game_day', models.IntegerField(null=True, blank=True)),
                ('game_year', models.TextField(null=True, blank=True)),
                ('home_away', models.IntegerField(null=True, blank=True)),
                ('team', models.CharField(max_length=20, null=True, blank=True)),
                ('opp_team', models.CharField(max_length=20, null=True, blank=True)),
                ('win_loss', models.IntegerField(null=True, blank=True)),
                ('min', models.IntegerField(null=True, blank=True)),
                ('fgm', models.IntegerField(null=True, blank=True)),
                ('fga', models.IntegerField(null=True, blank=True)),
                ('fg_pct', models.FloatField(null=True, blank=True)),
                ('fg3m', models.IntegerField(null=True, blank=True)),
                ('fg3a', models.IntegerField(null=True, blank=True)),
                ('fg3_pct', models.FloatField(null=True, blank=True)),
                ('ftm', models.IntegerField(null=True, blank=True)),
                ('fta', models.IntegerField(null=True, blank=True)),
                ('ft_pct', models.FloatField(null=True, blank=True)),
                ('oreb', models.IntegerField(null=True, blank=True)),
                ('dreb', models.IntegerField(null=True, blank=True)),
                ('reb', models.IntegerField(null=True, blank=True)),
                ('ast', models.IntegerField(null=True, blank=True)),
                ('stl', models.IntegerField(null=True, blank=True)),
                ('blk', models.IntegerField(null=True, blank=True)),
                ('tov', models.IntegerField(null=True, blank=True)),
                ('foul', models.IntegerField(null=True, blank=True)),
                ('pts', models.IntegerField(null=True, blank=True)),
                ('plus_minus', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'game_log_2015',
                'managed': False,
            },
        ),
    ]
