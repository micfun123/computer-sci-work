import factorial

#find the probability of getting certain 8 cards from a deck of 52 cards
def binomial_probability(n, k):
    return factorial.factorial(n) / (factorial.factorial(k) * factorial.factorial(n - k))

print(binomial_probability(104, 8)) 