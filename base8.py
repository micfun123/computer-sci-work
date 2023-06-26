
#convert to base8
def base8(n):
    if n == 0:
        return 0
    else:
        return (n % 8) + 10 * base8(n // 8)
    
print(base8(10))
