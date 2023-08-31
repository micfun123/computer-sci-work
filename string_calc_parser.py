def string_calc_parser(equation):
    allowed_characters = "0123456789+-*/"
    equation = "".join(char for char in equation if char in allowed_characters)
    
    if equation == "":
        return 0

    result = 0
    current_number = ""
    operator = "+"
    num_start = 0
    
    for i, char in enumerate(equation):
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                num = int(current_number)
                if operator == "+":
                    result += num
                elif operator == "-":
                    result -= num
                elif operator == "*":
                    result *= num
                elif operator == "/":
                    result /= num
                current_number = ""
            if char in "+-*/":
                operator = char
    
    if current_number:
        num = int(current_number)
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            result /= num
    
    return result

def string_calc_parser_simple(equation):
    #turns "1+2" into 3 and "1+2+3" into 6 and "12 + 3" into 15
   #if not a digit or operator, remove it
    
    allowed_characters = "0123456789+-*/"
    for char in equation:
        if char not in allowed_characters:
            equation = equation.replace(char, "")
    if equation == "":
        return 0
    if equation == None:
        return 0
    tosolve = []
    for char in equation:
        if char.isdigit():
            tosolve.append(int(char))
        else:
            tosolve.append(char)
    #join the digits together
    current_number = ""
    new_list = []
    for item in tosolve:
        if type(item) == int:
            current_number += str(item)
        else:
            new_list.append(int(current_number))
            new_list.append(item)
            current_number = ""
    new_list.append(int(current_number))
    #solve the equation using order of operations
    while len(new_list) > 1:
        for i in range(len(new_list)):
            if new_list[i] == "*":
                new_list[i] = new_list[i+1] *  new_list[i-1]
                new_list.pop(i-1)
                new_list.pop(i)
                break
            elif new_list[i] == "/":
                new_list[i] = new_list[i-1] / new_list[i+1]
                new_list.pop(i-1)
                new_list.pop(i)
                break
            elif new_list[i] == "+":
                new_list[i] = new_list[i-1] + new_list[i+1]
                new_list.pop(i-1)
                new_list.pop(i)
                break
            elif new_list[i] == "-":
                new_list[i] = new_list[i-1] - new_list[i+1]
                new_list.pop(i-1)
                new_list.pop(i)
                break

    return new_list[0]


# Test cases
print(string_calc_parser("1+2"))    # Output: 3
print(string_calc_parser("1+2+3"))  # Output: 6
print(string_calc_parser("12 + 3")) # Output: 15
