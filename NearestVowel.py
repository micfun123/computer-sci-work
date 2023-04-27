#Nearest Vowel
#
#Given a letter, created a function which returns the nearest vowel to the letter. If two vowels are equidistant to the given letter, return the earlier vowel.
#Examples
#
#nearestVowel("b") ➞ "a"
#
#nearestVowel("s") ➞ "u"
#
#nearestVowel("c") ➞ "a"
#
#nearestVowel("i") ➞ "i"
#
#Notes
#
#    All letters will be given in lowercase.
#    There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".

Vowels = ['a', 'e', 'i', 'o', 'u']

def nearestVowel(letter):
    if letter in Vowels:
        return letter
    else:
        for current_letter in range(1, 26):
            if chr(ord(letter) + current_letter) in Vowels:
                return chr(ord(letter) + current_letter)
            elif chr(ord(letter) - current_letter) in Vowels:
                return chr(ord(letter) - current_letter)

        
print(nearestVowel('z'))