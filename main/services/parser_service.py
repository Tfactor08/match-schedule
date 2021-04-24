from main.parser import main
from main.models import Match


def update_data(league: str) -> None:
    """Updates data"""

    matches = get_matches(league)

    Match.objects.filter(league=league).delete()

    for match in matches:
        Match.objects.create(first_team=match['teams'][0], second_team=match['teams'][1],
                                date=match['date'], time=match['time'], league=league)                          


def is_data_relevant(league: str) -> bool:
    """Returns false if data isn't relevant and true if it is"""

    matchParser = main.MatchParser(league)
    matches = matchParser.parse()

    if matches[-1]['date'] != None:
        return True

    return False


def get_matches(league: str) -> list:
    """Returns mathes"""

    matchParser = main.MatchParser(league)
    matches = matchParser.parse()

    return matches
