from django.conf.urls import url,patterns,include
from . import views

urlpatterns = [
  url(r'^$', views.basic_stats, name='basicstats'),
  url(r'(?P<p_id>\d+)/$', views.game_log, name='gamelog'),
  url(r'^fantasy/', views.fantasy_rankings, name='fantasy'),
  url(r'^userrank/vote/$', views.vote, name='vote'),
  url(r'^userrank/', views.user_rankings, name='user_rank'),
  url(r'^learning/', views.stats_learning, name='learning'),
  url(r'^about/', views.about, name='about'),
]