from django.contrib import admin
from .models import Player2015AverageStat, GameLog2015, IdPlayer, stdev2015
# Register your models here.

admin.site.register(Player2015AverageStat)
admin.site.register(GameLog2015)
admin.site.register(IdPlayer)
admin.site.register(stdev2015)