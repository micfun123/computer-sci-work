array = [20,2,6,12,8]

def calculate(array):
    total = 0
    add = True
    top = len(array)
    if top == 0:
        return ("Stack is empty")
    else:
        total = array[top - 1]
        print(total)
        top = top - 1
        while top > 0:
            if add:
                total = total + array[top - 1]
                print(f"current array value: {array[top - 1]}")
                print(total)
                add = False
            else:
                total = total - array[top - 1]
                print(f"current array value: {array[top - 1]}")
                add = True
            top = top - 1
        return total
    
print(calculate(array))

