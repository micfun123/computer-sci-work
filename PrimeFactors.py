

def divisors(integer):
    factors = []
    for i in range(2,integer):
        if integer % i == 0:
            factors.append(i)
    if factors == []:
        return f'{integer} is prime'
    return factors

print(divisors(12)) #should return [2,3,4,6]
print(divisors(25)) #should return [5]
print(divisors(13)) #should return "13 is prime"
