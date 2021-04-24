from django.shortcuts import render

from .models import Match, League
from .parser import main
from .services.parser_service import update_data, is_data_relevant


def index(request):

    leagues = League.objects.all()

    context = {
        'leagues': leagues
    }

    return render(request, 'main/index.html', context=context)

def matches(request, league):

    if not is_data_relevant(league):
        update_data(league)

    context = {
        'matches': Match.objects.filter(league=league)
    }

    return render(request, 'main/matches.html', context=context)

def match_detail(request, matchid):

    match = Match.objects.get(id=matchid)

    context = {
        'match': match
    }

    return render(request, 'main/detail.html', context=context)
