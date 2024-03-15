brackets = "()[]{}"

def validate(s):
    while True:
        if '()' in s:
            s = s.replace ( '()' , '' )
        elif '{}' in s:
            s = s.replace ( '{}' , '' )
        elif '[]' in s:
            s = s.replace ( '[]' , '' )
        else:
            break
    return s == ''



print(validate(brackets))