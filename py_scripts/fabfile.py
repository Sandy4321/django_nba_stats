from fabric.api import local
from fabric.context_managers import cd
def hello():
    print("Hello world!");

def remove():
    local("rm -rf /home/fred/django/github/django_nba_stats/nba_analysis")

def copy():
    local("cp -r /home/fred/django/nba_analysis  /home/fred/django/github/django_nba_stats/")

def add():
    with cd("/home/fred/django/github/django_nba_stats"):
        local("git add *")

def update():
    remove()
    copy()
    add()
