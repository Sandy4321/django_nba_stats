# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_userrankings2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthUsersocialauth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=32)),
                ('uid', models.CharField(max_length=255)),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'social_auth_usersocialauth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserVotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=255, null=True, blank=True)),
                ('provider', models.CharField(max_length=32, null=True, blank=True)),
                ('player_id', models.IntegerField(null=True, blank=True)),
                ('voted', models.IntegerField(null=True, blank=True)),
                ('up_down', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'user_votes',
                'managed': False,
            },
        ),
    ]
