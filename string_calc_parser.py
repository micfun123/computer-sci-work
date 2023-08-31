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

# Test cases
print(string_calc_parser("1+2"))    # Output: 3
print(string_calc_parser("1+2+3"))  # Output: 6
print(string_calc_parser("12 + 3")) # Output: 15
