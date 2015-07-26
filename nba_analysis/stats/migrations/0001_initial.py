# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season_id', models.IntegerField(null=True, blank=True)),
                ('player_id', models.IntegerField(null=True, blank=True)),
                ('game_id', models.IntegerField(null=True, blank=True)),
                ('game_month', models.TextField(null=True, blank=True)),
                ('game_day', models.TextField(null=True, blank=True)),
                ('game_year', models.TextField(null=True, blank=True)),
                ('home_away', models.IntegerField(null=True, blank=True)),
                ('team', models.TextField(null=True, blank=True)),
                ('opp_team', models.TextField(null=True, blank=True)),
                ('win_loss', models.IntegerField(null=True, blank=True)),
                ('min', models.IntegerField(null=True, blank=True)),
                ('fgm', models.IntegerField(null=True, blank=True)),
                ('fga', models.IntegerField(null=True, blank=True)),
                ('fg_pct', models.IntegerField(null=True, blank=True)),
                ('fg3m', models.IntegerField(null=True, blank=True)),
                ('fg3a', models.IntegerField(null=True, blank=True)),
                ('fg3_pct', models.IntegerField(null=True, blank=True)),
                ('ftm', models.IntegerField(null=True, blank=True)),
                ('fta', models.IntegerField(null=True, blank=True)),
                ('ft_pct', models.IntegerField(null=True, blank=True)),
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
                'db_table': 'GAME_LOG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IdPlayer',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.TextField(null=True, blank=True)),
                ('middle_name', models.TextField(null=True, blank=True)),
                ('last_name', models.TextField(null=True, blank=True)),
                ('from_year', models.IntegerField(null=True, blank=True)),
                ('to_year', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'id_player',
                'managed': False,
            },
        ),
    ]
