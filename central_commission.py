import random
import math

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

from voter import Voter


class CentralCommission:
    def __init__(self) -> None:
        self.rsa_keys = {}
        self.dsa_keys = {}

    @staticmethod
    def create_voters() -> list:
        voters = []
        for _ in range(4):
            voters.append(Voter(random.randint(10, 50)))

        return voters

    def create_candidates(self) -> list:
        candidates = []
        for _ in range(2):
            while True:
                candidate_id = random.randint(10, 50)
                if not self.is_prime(candidate_id):
                    break

            candidates.append(candidate_id)

        return candidates

    def generate_dsa_keys(self, voters: tuple) -> None:
        for voter in voters:
            private_key = DSA.generate(1024)
            public_key = private_key.publickey()
            self.dsa_keys[voter.id] = private_key, public_key

    def generate_rsa_keys(self, voters: tuple) -> None:
        for voter in voters:
            self.rsa_keys[voter.id] = self.generate_keypair()

    @staticmethod
    def generate_keypair():
        p = 139
        q = 659
        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randrange(2, phi)
        while math.gcd(e, phi) != 1:
            e = random.randrange(2, phi)

        d = pow(e, -1, phi)

        return (n, e), (n, d)

    @staticmethod
    def encrypt(public_key, message):
        n, e = public_key

        return pow(message, e, n)

    @staticmethod
    def decrypt(private_key, cipher_message):
        n, d = private_key

        return pow(cipher_message, d, n)

    @staticmethod
    def is_prime(number: int) -> bool:
        if number <= 1:
            return True
        elif number == 2:
            return True
        elif number % 2 == 0:
            return True
        else:
            # Check for factors up to the square root of the number
            for i in range(3, int(number ** 0.5) + 1, 2):
                if number % i == 0:
                    return False
            return True
