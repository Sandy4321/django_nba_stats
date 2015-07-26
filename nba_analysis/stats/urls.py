from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.basic_stats, name='basicstats'),
  url(r'(?P<p_id>\d+)/$', views.game_log, name='gamelog'),
  url(r'^fantasy/', views.fantasy, name='fantasy'),
]