from random import choice


class Voter:
    def __init__(self, self_id: int) -> None:
        self.id = self_id
        self.vote = None
        self.factors = []
        self.ballots = []

    def make_choice(self, candidates: list) -> None:
        self.vote = choice(candidates)

    def split_to_factors(self) -> None:
        factors = []
        for i in range(1, int(self.vote / 2) + 1):
            if self.vote % i == 0:
                factors.append(i)

        self.factors.append(choice(factors))
        self.factors.append(self.vote // self.factors[0])

    def create_ballots(self) -> None:
        self.ballots.append({"vote": self.vote, "factors": self.factors[0]})
        self.ballots.append({"vote": self.vote, "factors": self.factors[1]})
