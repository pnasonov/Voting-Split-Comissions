from central_commission import CentralCommission

from comission import Commission

central_commission = CentralCommission()

# creating voters with ids
voters = tuple(central_commission.create_voters())
for i, voter in enumerate(voters):
    print(f"Voter {i + 1} ID: {voter.id}")

# creating candidates with ids
candidates = tuple(central_commission.create_candidates())
for i in range(len(candidates)):
    print(f"Candidate {i + 1} ID: {candidates[i]}")

print("\nVoting process...")
# voter making his choice
for i, voter in enumerate(voters):
    voter.make_choice(candidates)
    print(f"Voter {i + 1} has voted for", voter.vote)

print("\nDividing to factors:")
# voter split id of his choice into two random factors
for i, voter in enumerate(voters):
    voter.split_to_factors()
    print(f"Voter {i + 1} factors", voter.factors)

# central commission creates rsa,dsa keys for all voters
central_commission.generate_rsa_keys(voters)
central_commission.generate_dsa_keys(voters)

print("\nEncrypting RSA")
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
    print(f"Encrypted message voter {i + 1}",
          f"{voter.ballot_a[0]}",
          f"{voter.ballot_b[0]}")

print("\nSigning ballots:")
# signing ballots
for i, voter in enumerate(voters):
    voter.ballot_a.append(voter.sign_message(
        voter.ballot_a[0], central_commission.dsa_keys[voter.id][0]
    ))
    voter.ballot_b.append(voter.sign_message(
        voter.ballot_b[0], central_commission.dsa_keys[voter.id][0]
    ))
    print(f"DSA {i + 1} voter signed message\n"
          f"{voter.ballot_a[2]}\n{voter.ballot_b[2]}")

# sending ballots to commissions
first_commission = Commission(
    {k: v[1] for k, v in central_commission.dsa_keys.items()}
)
first_commission.check_ballots([voter.ballot_a for voter in voters])
print(f"\nFirst commission publishing results of sign check "
      f"{first_commission.collected}")

second_commission = Commission(
    {k: v[1] for k, v in central_commission.dsa_keys.items()}
)
second_commission.check_ballots([voter.ballot_b for voter in voters])
print(f"\nSecond commission publishing results of sign check "
      f"{second_commission.collected}\n")

# central commission collecting votes
result = central_commission.count_result(first_commission.collected,
                                         second_commission.collected)

print(f"\nElection winner: {result}")
