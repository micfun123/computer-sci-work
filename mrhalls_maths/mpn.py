# p^n + 3600 = m^2
# p is prime , n and m are integers

tosolve = 200

solution = []


def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for p in range(1, tosolve):
    if isprime(p):
        for n in range(1, tosolve):
            for m in range(1, tosolve):
                if p**n + 3600 == m**2:
                    solution.append((p, n, m))

print(solution)
