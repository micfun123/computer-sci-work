keyword = str(input("Enter a keyword: "))
phrase = str(input("Enter a phrase: "))

def keyword_cipher(keyword, phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.lower()
    keyword = keyword.replace(" ","")
    phrase = phrase.lower()
    key = ""
    for letter in keyword:
        if letter not in key:
            key += letter
    for letter in alphabet:
        if letter not in key:
            key += letter
    cipher = "" 
    for letter in phrase:
        if letter in alphabet:
            cipher += key[alphabet.index(letter)]
        else:
            cipher += letter

    return cipher

print(keyword_cipher(keyword,phrase))

