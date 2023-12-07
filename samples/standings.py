from enum import Enum

class ResultType(Enum):
    WIN = 0
    DRAW = 1
    LOSE = 2

scoretable = {}

def report_result(team: str, result_type: ResultType):
    if team not in scoretable:
        scoretable[team] = {ResultType.WIN: 0, ResultType.DRAW: 0, ResultType.LOSE: 0}
    scoretable[team][result_type] += 1

def get_score(team: str) -> int:
    team_results = scoretable[team]
    sum = 0
    for type in team_results:
        sum += __get_points_for_result(type) * team_results[type]
    return sum

def __get_points_for_result(result_type: ResultType) -> int:
    if result_type == ResultType.WIN:
        return 3
    elif result_type == ResultType.DRAW:
        return 1
    return 0
