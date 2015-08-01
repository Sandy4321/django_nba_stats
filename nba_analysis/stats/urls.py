from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.basic_stats, name='basicstats'),
  url(r'(?P<p_id>\d+)/$', views.game_log, name='gamelog'),
  url(r'^fantasy/', views.fantasy_rankings, name='fantasy'),
  url(r'^userrank/upvote/$', views.vote, name='vote'),
  url(r'^userrank/', views.user_rankings, name='user_rank'),
]