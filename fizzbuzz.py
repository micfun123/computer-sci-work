# Description: FizzBuzz program


def fizzBuzz(n: int):
    output = []
    string = ""
    if n % 3 == 0:
        string = string + "Fizz"
    if n % 5 == 0:
        string = string + "Buzz"
    if string == "":
        string = n
    output.append(string)
    string = ""
    return output


for i in range(1, 101):
    print(fizzBuzz(i))
