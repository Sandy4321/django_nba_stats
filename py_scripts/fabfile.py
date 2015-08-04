from fabric.api import local
from fabric.context_managers import cd
def hello():
    print("Hello world!");

def update():
    local("rm -rf /home/fred/django/github/django_nba_stats/nba_analysis")
    local("cp -r /home/fred/django/nba_analysis  /home/fred/django/github/django_nba_stats/")
    with cd("/home/fred/django/github/django_nba_stats"):
        local("git add *")
