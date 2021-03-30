from django.shortcuts import render

from .models import Match, League
from .parser import main

def index(request):

    leagues = League.objects.all()

    context = {
        'leagues': leagues
    }

    return render(request, 'main/index.html', context=context)

def matches(request, league):

    matchParser = main.MatchParser(league)
    matches = matchParser.parse()
    if matches[-1]['date'] != None:
        Match.objects.all().delete()
        for match in matches:
            Match.objects.create(first_team=match['teams'][0], second_team=match['teams'][1],
                                    date=match['date'], time=match['time'], league=league)

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
