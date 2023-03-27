# how many of the first million terms of 1/sqrt(n) have a decimal with the first non-zero digit equal to 1?
import math

def main():
    count = 0
    truecount = 0
    for n in range(1, 1000001):
        if int(str(math.sqrt(n))[0]) == 1:
            print(str(math.sqrt(n)))
            count += 1
        truecount += 1
    print(count)
    print(truecount)
    


if __name__ == "__main__":
    main()
