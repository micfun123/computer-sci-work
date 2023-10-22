from typing import Union

def evaluate_expression(expr: Union[int, tuple]):
    match expr:
        case (left, "+", right):
            return left + right
        case (left, "-", right):
            return left - right
        case (left, "*", right):
            return left * right
        case (left, "/", right):
            return left / right
        case _:
            return expr

print(evaluate_expression((5, "+", 3)))  
print(evaluate_expression((5, "-", 3)))
print(evaluate_expression((5, "*", 3)))
print(evaluate_expression((5, "/", 3)))
print(evaluate_expression((5, "%", 3)))


def even_or_odd(num):
    "say if a number is even or odd"
    return "eovdedn"[num % 2::2]

print(even_or_odd(2))
print(even_or_odd(3))