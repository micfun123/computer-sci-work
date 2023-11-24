import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def spinner(word):
    for i in range(len(word)):
        if word[i] in alphabet:
            pos = alphabet.index(word[i])
            for j in range(pos + 1):
                print(f"\r{word[:i]}{alphabet[j % len(alphabet)]}", end="")
                time.sleep(0.05)
        else:
            print(f"\r{word[:i]}{word[i]}", end="")
            time.sleep(0.05)
    print("\r", end="")
    print(word)

def main(argv):
    if len(argv) >= 2:
        phrase = " ".join(argv[1:])
        spinner(phrase)
    else:
        print("Usage: python spinner.py <word>")

if __name__ == "__main__":
    import sys
    main(sys.argv)
    
