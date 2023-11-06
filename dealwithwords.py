# open words.txt

file = open("words.txt", "r")  # r is for read, w is for write, a is for append
print(file.read())
print(file.readline())
# when finnished with file, close it
file.close()
