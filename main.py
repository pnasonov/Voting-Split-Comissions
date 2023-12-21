from central_commission import CentralCommission

central_commission = CentralCommission()

# creating voters with ids
voters = tuple(central_commission.create_voters())
# print([voter.__dict__ for voter in voters])

# creating candidates with ids
candidates = tuple(central_commission.create_candidates())

# voter making his choice
for i, voter in enumerate(voters):
    voter.make_choice(candidates)
    print(f"Voter {i + 1} has voted for", voter.vote)

# voter split id of his choice into two random factors
for voter in voters:
    voter.split_to_factors()
    print(voter.factors)

# central commission creates rsa keys for all voters
central_commission.generate_rsa_keys(voters)

# voter encrypts 2 ballots with public rsa key and add id
for i, voter in enumerate(voters):
    voter.ballot_a.append(central_commission.encrypt(
        central_commission.rsa_keys[voter.id][0],
        voter.factors[0]
    ))
    voter.ballot_a.append(voter.id)

    voter.ballot_b.append(central_commission.encrypt(
        central_commission.rsa_keys[voter.id][0],
        voter.factors[1]
    ))
    voter.ballot_b.append(voter.id)
    print(f"Encrypted message and voter {i + 1} ID",
          voter.ballot_a,
          voter.ballot_b)

# singing ballots