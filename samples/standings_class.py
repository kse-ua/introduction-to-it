from enum import Enum

class ResultType(Enum):
    WIN = 0
    DRAW = 1
    LOSE = 2

class ScoreTableRecord:

    def __init__(self):
        self.wins = 0
        self.loses = 0
        self.draws = 0

    def add_result(self, result_type: ResultType):
        if result_type == ResultType.WIN:
            self.wins += 1
        elif result_type == ResultType.DRAW:
            self.draws += 1
        else:
            self.loses += 1

    def get_score(self) -> int:
        return self.wins * 3 + self.draws


scoretable = {}

def report_result(team: str, result_type: ResultType):
    if team not in scoretable:
        scoretable[team] = ScoreTableRecord()
    scoretable[team].add_result(result_type)

def get_score(team: str) -> int:
    return scoretable[team].get_score()

