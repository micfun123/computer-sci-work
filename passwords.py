import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
pw_length = 12
mypw = ""

def pw_gen():
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]


    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2)
        mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index+1:]


    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2,len(mypw))
        mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]

    punctuation = "!@#$%^&*()_+~`|}{[]\:;?><,./'"
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2,len(mypw))
        mypw = mypw[0:replace_index] + random.choice(punctuation) + mypw[replace_index+1:]

print(mypw)
