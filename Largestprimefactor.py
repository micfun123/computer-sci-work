#The prime factors of 13195 are 5, 7, 13 and 29. target 600851475143

number = int(input("Enter a number: "))
primefactors = []
for i in range(2, number):
    print(i)
    if number % i == 0:
        primefactors.append(i)
        number = number / i

print(primefactors)
