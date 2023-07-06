
cars="CCCCCBBBBOOOOBBCCCBCCCCBBBBBCCOOOCCCCCCC"

def longest_continuse(cars):
    #find longest continuse amount of C
    max_c=0
    currnt_c=0
    for i in range(len(cars)):
        if cars[i]=="C":
            currnt_c+=1
        else:
            if currnt_c>max_c:
                max_c=currnt_c
            currnt_c=0
    if currnt_c>max_c:
        max_c=currnt_c
    return max_c
