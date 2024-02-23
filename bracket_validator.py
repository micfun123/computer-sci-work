brackets = "({([])})"

def validate(str):
    while True:
        if '()' in str:
            str = str.replace ( '()' , '' )
        elif '{}' in str:
            str = str.replace ( '{}' , '' )
        elif '[]'in str:
            str = str.replace ( '[]' , '' )
        else:
            return not str
    


print(validate(brackets))