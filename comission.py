from Crypto.Hash import SHA256
from Crypto.Signature import DSS


class Commission:
    def __init__(self, dsa_public_keys: dict) -> None:
        self.dsa_public_keys = dsa_public_keys
        self.checked_ids = []
        self.collected = {}

    @staticmethod
    def verify_sign(message, signature, public_key):
        h = SHA256.new(bytes(message))
        verifier = DSS.new(public_key, 'fips-186-3')
        try:
            verifier.verify(h, signature)
            return True
        except ValueError:
            raise ValueError("Error while signature verification")

    def check_ballots(self, ballots: list) -> None:
        for ballot in ballots:
            if self.verify_sign(
                    message=ballot[0],
                    signature=ballot[2],
                    public_key=self.dsa_public_keys[ballot[1]]
            ):
                if ballot[1] not in self.checked_ids:
                    self.checked_ids.append(ballot[1])
                    self.collected[ballot[1]] = ballot[0]
                else:
                    raise ValueError(ballot[1])
