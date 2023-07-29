
def string_calc_parser(equation):
    #turns "1+2" into 3 and "1+2+3" into 6 and "12 + 3" into 15
    numbers = []
    operators = []
    current_number = ""
    for char in equation:
        if char.isdigit():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ""
            operators.append(char)
    numbers.append(int(current_number))
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i+1]
        elif operators[i] == "-":
            result -= numbers[i+1]
        elif operators[i] == "*":
            result *= numbers[i+1]
        elif operators[i] == "/":
            result /= numbers[i+1]

    return result

print(string_calc_parser("1+2"))
print(string_calc_parser("12+3"))
        