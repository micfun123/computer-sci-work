import string

userinpute = str(input("Enter a sentance: "))


def compress_via_dictionary(str) -> str:
    istringids = []
    Words = []
    str = str.lower()
    for i in string.punctuation:
        str = str.replace(i, '')
    for i in str.split():
        if i in Words:
            pass
        else:
            Words.append(i)
    for j in str.split():
        istringids.append(Words.index(j))
    return istringids , Words
    

def extract_via_dictionary(idarray,wordarray) -> dict:
    sentance = []
    print(idarray)
    for i in idarray:
        i = int(i)
        sentance.append(wordarray[i])

    return " ".join(sentance)
        #get last word id and add a new id
ids,words = compress_via_dictionary(userinpute)
print(extract_via_dictionary(ids,words))