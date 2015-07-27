from django.shortcuts import get_object_or_404, render
from .models import Player2015AverageStat, GameLog2015, IdPlayer, stdev2015, UserRankings2015

def basic_stats(request):
    players = Player2015AverageStat.objects.all()
    return render(request, 'stats/stats_main.html', {'players': players})

def game_log(request, p_id):
    player_name = get_object_or_404(IdPlayer, id=p_id)
    player_avg = get_object_or_404(Player2015AverageStat, player_id=p_id)
    gamelog = GameLog2015.objects.all().filter(player_id=p_id)
    return render(request, 'stats/game_log.html', {'gamelog': gamelog, 'player_name': player_name, 'player_avg': player_avg})

def fantasy_rankings(request):
    players = sorted(stdev2015.objects.all(), key=lambda player: player.getSum(), reverse=True)
    return render(request, 'stats/fantasy_ranking.html', {'players': players})

def user_rankings(request):
    players = sorted(UserRankings2015.objects.all(), key=lambda player: player.user_rank, reverse=True)
    return render(request, 'stats/user_rankings.html', {'players': players})