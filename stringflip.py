from parse import parse

add = "hey man"
main = f"I dont know what to say {add} ok cool"
print(main)
def unformat(string):
    #extract the string from the f-string
    purestring = parse("I dont know what to say {} ok cool", string)
    return purestring[0]


print(unformat(main))
