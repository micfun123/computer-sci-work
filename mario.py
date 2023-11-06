def pyramid(height):
    for i in range(1, height + 1):
        for space in range(height - i):
            print(" ", end="")
        for hash in range(i):
            print("#", end="")
        print(" ", end="")
        for hash in range(i):
            print("#", end="")
        print()


pyramid(4)
