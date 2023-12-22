from random import choice

from Crypto.Hash import SHA256
from Crypto.Signature import DSS


class Voter:
    def __init__(self, self_id: int) -> None:
        self.id = self_id
        self.vote = None
        self.factors = []
        self.ballot_a = []
        self.ballot_b = []

    def make_choice(self, candidates: list) -> None:
        self.vote = choice(candidates)

    def split_to_factors(self) -> None:
        factors = []
        for i in range(2, int(self.vote / 2) + 1):
            if self.vote % i == 0:
                factors.append(i)

        self.factors.append(choice(factors))
        self.factors.append(self.vote // self.factors[0])

    @staticmethod
    def sign_message(message, private_key):
        hash_obj = SHA256.new(bytes(message))
        signer = DSS.new(private_key, 'fips-186-3')
        signature = signer.sign(hash_obj)
        return signature
