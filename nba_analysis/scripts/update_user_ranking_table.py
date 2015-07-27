'''
previous user ranking database did not have a column for user UserRankings2015
before executing this script a table (user_rankings_2015) in MySQL was made, same schema and info as fantasy_stdev_2015.
the only addition is the new column called user_rank, which is going to be based off user upvote/downvotes.
this script populates the ranking based on the default stddev ranking (user_rank will span from [1,450])
'''
from stats.models import UserRankings2015
players = sorted(UserRankings2015.objects.all(), key=lambda player: player.getSum(), reverse=True)
rank_iter = len(players)
for player in players:
  print(rank_iter)
  player.user_rank = rank_iter
  player.save()
  rank_iter -= 1
