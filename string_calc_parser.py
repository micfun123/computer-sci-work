
def string_calc_parser(equation):
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

           
    
    

def test(enter,expected):
    out = string_calc_parser(enter)
    if out != expected: 
        print( f"tested for {enter} and failed. \n We got {out} \n We expected {expected}")
    else:
        print(True)

test("1+2",3)
test("1+22",23)
test("1+2 2",23)
test("1",1)
test("2 *2",4)
test("   2 * 2-1",3)
test("  ",0)

