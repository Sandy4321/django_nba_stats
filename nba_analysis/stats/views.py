from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from .models import Player2015AverageStat, GameLog2015, IdPlayer, stdev2015, UserRankings2015

def basic_stats(request):
    players = Player2015AverageStat.objects.all()
    login_context = RequestContext(request,{'user':request.user})

    return render(request, 'stats/stats_main.html', {'players': players}, context_instance=login_context)

def game_log(request, p_id):
    player_name = get_object_or_404(IdPlayer, id=p_id)
    player_avg = get_object_or_404(Player2015AverageStat, player_id=p_id)
    gamelog = GameLog2015.objects.all().filter(player_id=p_id)
    login_context = RequestContext(request,{'user':request.user})
    return render(request, 'stats/game_log.html', {'gamelog': gamelog, 'player_name': player_name, 'player_avg': player_avg}, context_instance=login_context)

def fantasy_rankings(request):
    players = sorted(stdev2015.objects.all(), key=lambda player: player.getSum(), reverse=True)
    login_context = RequestContext(request,{'user':request.user})
    return render(request, 'stats/fantasy_ranking.html', {'players': players}, context_instance=login_context)

def user_rankings(request):
    players = sorted(UserRankings2015.objects.all(), key=lambda player: player.user_rank, reverse=True)
    login_context = RequestContext(request,{'request': request, 'user': request.user})
    return render(request, 'stats/user_rankings.html', {'players': players}, context_instance=login_context)

def vote(request):
    if request.is_ajax():
        if request.method == 'POST':
            player_id = request.POST.get('player_id')
            player = get_object_or_404(UserRankings2015, id=player_id)
            updown = request.POST.get('voteType')
            count = int(request.POST.get('count'))
            if updown == "up":
                player.upvote(count=count)
            elif updown == "down":
                player.downvote(count=count)

    else:
        player_id = request.POST.get('player_id')
        player = get_object_or_404(UserRankings2015, id=player_id)
        updown = request.POST.get('voteType')
        count = 1
        if updown == "up":
            player.upvote(count = count)
        elif updown == "down":
            player.downvote(count = count)

    return HttpResponseRedirect(" ")
