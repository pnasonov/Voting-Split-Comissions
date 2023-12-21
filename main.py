from central_commission import CentralCommission

central_commission = CentralCommission()

# creating voters with ids
voters = tuple(central_commission.create_voters())
# print([voter.__dict__ for voter in voters])

# creating candidates with ids
candidates = tuple(central_commission.create_candidates())

# voter making his choice
for voter in voters:
    voter.make_choice(candidates)
    print(voter.vote)

# voter split id of his choice into two random factors
for voter in voters:
    voter.split_to_factors()
    print(voter.factors)

