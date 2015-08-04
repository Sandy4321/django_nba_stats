from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from .models import Player2015AverageStat, GameLog2015, IdPlayer, stdev2015, UserRankings2015, AuthUser, UserVotes

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
            user = get_object_or_404(AuthUser, username=request.user)
            unvote = request.POST.get('unvote')

            #add a unvote option here later
            prevVote = UserVotes.objects.all().filter(user_id=user.id, player_id = player_id)
            if updown == "up":
                player.upvote(count=count)
                if not prevVote: #player was not voted by this user before
                    print("new up entry")
                    vote_update = UserVotes(user_id=user.id, player_id=player_id, voted=True, up_down=True)
                    vote_update.save()
                else:
                    if unvote == "true":
                        print("remove up entry")
                        vote_update = UserVotes(id=prevVote[0].id, user_id=user.id, player_id=player_id, voted=False, up_down=True)
                        vote_update.save(force_update=True)
                    else:
                        print("update up entry")
                        vote_update = UserVotes(id=prevVote[0].id, user_id=user.id, player_id=player_id, voted=True, up_down=True)
                        vote_update.save(force_update=True)
                print("Saved Up")

            elif updown == "down":
                player.downvote(count=count)
                if not prevVote:
                    print("new down entry")
                    vote_update = UserVotes(user_id=user.id, player_id=player_id, voted=True, up_down=False)
                    vote_update.save()
                else:
                    if unvote == "true":
                        print("remove down entry")
                        vote_update = UserVotes(id=prevVote[0].id, user_id=user.id, player_id=player_id, voted=False, up_down=False)
                        vote_update.save(force_update=True)
                    else:
                        print("update down entry")
                        vote_update = UserVotes(id=prevVote[0].id, user_id=user.id, player_id=player_id, voted=True, up_down=False)
                        vote_update.save(force_update=True)
                print("Saved Down")

    #if user did not enable javascript or jquery or something
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
