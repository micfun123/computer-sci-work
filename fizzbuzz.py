# Description: FizzBuzz program


def fizzBuzz(n: int):
    output = []
    for i in range(1, n+1):
            string = ""
            if i % 3 == 0:
                string = string + "Fizz" 
            if i % 5 == 0:
                string = string + "Buzz"
            if string == "":
                string = i

            output.append(string)
            string = ""
    return output


print(fizzBuzz(15))