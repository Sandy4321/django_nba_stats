# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django import forms

class Player2015AverageStat(models.Model):
    player_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    games_played = models.IntegerField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    fgm = models.FloatField(blank=True, null=True)
    fga = models.FloatField(blank=True, null=True)
    fg_pct = models.FloatField(blank=True, null=True)
    fg3m = models.FloatField(blank=True, null=True)
    fg3a = models.FloatField(blank=True, null=True)
    fg3_pct = models.FloatField(blank=True, null=True)
    ftm = models.FloatField(blank=True, null=True)
    fta = models.FloatField(blank=True, null=True)
    ft_pct = models.FloatField(blank=True, null=True)
    oreb = models.FloatField(blank=True, null=True)
    dreb = models.FloatField(blank=True, null=True)
    reb = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)
    stl = models.FloatField(blank=True, null=True)
    blk = models.FloatField(blank=True, null=True)
    tov = models.FloatField(blank=True, null=True)
    atr = models.FloatField(blank=True, null=True)
    foul = models.FloatField(blank=True, null=True)
    pts = models.FloatField(blank=True, null=True)
    plus_minus = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.first_name) + " " +str(self.last_name)

    class Meta:
        managed = False
        db_table = 'avg_2015'
        ordering = ['-pts', 'last_name']

class GameLog2015(models.Model):
    season_id = models.IntegerField(blank=True, null=True)
    player_id = models.IntegerField(blank=True, null=True)
    game_id = models.IntegerField(blank=True, null=True)
    game_month = models.CharField(max_length=10, blank=True, null=True)
    game_day = models.IntegerField(blank=True, null=True)
    game_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    home_away = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=20, blank=True, null=True)
    opp_team = models.CharField(max_length=20, blank=True, null=True)
    win_loss = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    fgm = models.IntegerField(blank=True, null=True)
    fga = models.IntegerField(blank=True, null=True)
    fg_pct = models.FloatField(blank=True, null=True)
    fg3m = models.IntegerField(blank=True, null=True)
    fg3a = models.IntegerField(blank=True, null=True)
    fg3_pct = models.FloatField(blank=True, null=True)
    ftm = models.IntegerField(blank=True, null=True)
    fta = models.IntegerField(blank=True, null=True)
    ft_pct = models.FloatField(blank=True, null=True)
    oreb = models.IntegerField(blank=True, null=True)
    dreb = models.IntegerField(blank=True, null=True)
    reb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    foul = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.player_id)

    class Meta:
        managed = False
        db_table = 'game_log_2015'


class IdPlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    from_year = models.IntegerField(blank=True, null=True)
    to_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.first_name) + " " +str(self.last_name)

    class Meta:
        managed = False
        db_table = 'id_player'

class stdev2015(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    games_played = models.IntegerField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    fgm = models.FloatField(blank=True, null=True)
    fga = models.FloatField(blank=True, null=True)
    fg_pct = models.FloatField(blank=True, null=True)
    fg3m = models.FloatField(blank=True, null=True)
    fg3a = models.FloatField(blank=True, null=True)
    fg3_pct = models.FloatField(blank=True, null=True)
    ftm = models.FloatField(blank=True, null=True)
    fta = models.FloatField(blank=True, null=True)
    ft_pct = models.FloatField(blank=True, null=True)
    oreb = models.FloatField(blank=True, null=True)
    dreb = models.FloatField(blank=True, null=True)
    reb = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)
    stl = models.FloatField(blank=True, null=True)
    blk = models.FloatField(blank=True, null=True)
    tov = models.FloatField(blank=True, null=True)
    atr = models.FloatField(blank=True, null=True)
    pts = models.FloatField(blank=True, null=True)

    def getSum(self):
        return self.games_played + self.fgm +\
            self.fg_pct + self.fg3m + self.fg3_pct + self.ftm +\
            self.ft_pct + self.reb + self.ast + self.stl + self.blk+\
            self.tov + self.atr + self.pts


    def __str__(self):
        return str(self.first_name) + " " +str(self.last_name)

    class Meta:
        managed = False
        db_table = 'fantasy_stdev_2015'

class UserRankings2015(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    games_played = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    fgm = models.FloatField(blank=True, null=True)
    fga = models.FloatField(blank=True, null=True)
    fg_pct = models.FloatField(blank=True, null=True)
    fg3m = models.FloatField(blank=True, null=True)
    fg3a = models.FloatField(blank=True, null=True)
    fg3_pct = models.FloatField(blank=True, null=True)
    ftm = models.FloatField(blank=True, null=True)
    fta = models.FloatField(blank=True, null=True)
    ft_pct = models.FloatField(blank=True, null=True)
    oreb = models.FloatField(blank=True, null=True)
    dreb = models.FloatField(blank=True, null=True)
    reb = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)
    stl = models.FloatField(blank=True, null=True)
    blk = models.FloatField(blank=True, null=True)
    tov = models.FloatField(blank=True, null=True)
    atr = models.FloatField(blank=True, null=True)
    pts = models.FloatField(blank=True, null=True)
    user_rank = models.IntegerField(blank=True, null=True)

    def getSum(self):
        return self.games_played + self.fgm +\
            self.fg_pct + self.fg3m + self.fg3_pct + self.ftm +\
            self.ft_pct + self.reb + self.ast + self.stl + self.blk+\
            self.tov + self.atr + self.pts

    def upvote(self):
        self.user_rank += 1
        self.save()

    def downvote(self):
        self.user_rank -= 1
        self.save()

    class Meta:
        managed = False
        db_table = 'user_rankings_2015'