# p^n + 3600 = m^2
tosolve = 100

solution = []


for p in range(1, tosolve):
    for n in range(p+1, tosolve):
        for m in range(n+1, tosolve):
            if p**n + 3600 == m**2:
                solution.append(f"{p} , {n}, {m}")
            print(p,m,n)
    print("Row done")

print(solution)


