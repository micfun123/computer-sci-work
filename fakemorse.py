def morseEncode(x):
     
    # refer to the Morse table
    # image attached in the article
    if x is 'a':
        return ".-"
    elif x is 'b':
        return "-..."
    elif x is 'c':
        return "-.-."
    elif x is 'd':
        return "-.."
    elif x is 'e':
        return "."
    elif x is 'f':
        return "..-."
    elif x is 'g':
        return "--."
    elif x is 'h':
        return "...."
    elif x is 'i':
        return ".."
    elif x is 'j':
        return ".---"
    elif x is 'k':
        return "-.-"
    elif x is 'l':
        return ".-.."
    elif x is 'm':
        return "--"
    elif x is 'n':
        return "-."
    elif x is 'o':
        return "---"
    elif x is 'p':
        return ".--."
    elif x is 'q':
        return "--.-"
    elif x is 'r':
        return ".-."
    elif x is 's':
        return "..."
    elif x is 't':
        return "-"
    elif x is 'u':
        return "..-"
    elif x is 'v':
        return "...-"
    elif x is 'w':
        return ".--"
    elif x is 'x':
        return "-..-"
    elif x is 'y':
        return "-.--"
    elif x is 'z':
        return "--.."
    elif x is '1':
        return ".----";
    elif x is '2':
        return "..---";
    elif x is '3':
        return "...--";
    elif x is '4':
        return "....-";
    elif x is '5':
        return ".....";
    elif x is '6':
        return "-....";
    elif x is '7':
        return "--...";
    elif x is '8':
        return "---..";
    elif x is '9':
        return "----.";
    elif x is '0':
        return "-----";
 
s = input("Enter the text: ")
for i in s:
    morseEncode(s)