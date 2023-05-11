from math import comb

def binomial_expansion(expression, power):
    result = ""
    for k in range(power + 1):
        coefficient = comb(power, k)
        term_a = round(expression[0] ** (power - k), 2)
        term_b = round(expression[1] ** k, 2)
        term = round(coefficient * term_a * term_b, 2)
        result += f"{term} * {expression[2]}^{power - k} * {expression[3]}^{k} + "
    return result[:-3]  # Remove the extra "+ " at the end

# Test the function
expression = [1,2, "x", "y"]
power = 5
expansion = binomial_expansion(expression, power)
print(expansion)
