import random

from voter import Voter


class CentralCommission:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_voters() -> list:
        voters = []
        for _ in range(4):
            voters.append(Voter(random.randint(10, 50)))

        return voters

    @staticmethod
    def create_candidates() -> list:
        candidates = []
        for _ in range(2):
            candidates.append(random.randint(10, 50))

        return candidates
