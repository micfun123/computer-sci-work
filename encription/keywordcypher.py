keyword = str(input("Enter your key word: "))
phrase = str(input("Enter your phrase: "))


def encript_keyword_cipher(keyword, phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.lower()
    keyword = keyword.replace(" ", "")
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

    return str(cipher)


def dencript_keyword_cipher(keyword, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.lower()
    keyword = keyword.replace(" ", "")
    cipher = cipher.lower()
    key = ""
    for letter in keyword:
        if letter not in key:
            key += letter
    for letter in alphabet:
        if letter not in key:
            key += letter
    phrase = ""
    for letter in cipher:
        if letter in key:
            phrase += alphabet[key.index(letter)]
        else:
            phrase += letter
    return phrase


print(encript_keyword_cipher(keyword, phrase))
code = encript_keyword_cipher(keyword, phrase)
print(dencript_keyword_cipher(keyword, code))
