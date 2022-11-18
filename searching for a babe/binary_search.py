
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
names = ['apple', 'banana', 'car', 'cat', 'dinosaur', 'dogs', 'elephant', 'fish', 'giraffe', 'horse', 'human', 'ice cream', 'jelly', 'jhon', 'kangaroo', 'lion', 'mandy', 'michael', 'monkey', 'noodles', 'orange', 'panda', 'quail', 'rabbit', 'snake', 'tiger', 'umbrella', 'violin', 'watermelon', 'xylophone', 'yak', 'zebra', 'zoo']

def binary_search(names, name):
    start = 0
    end = len(names) - 1
    while start <= end:
        mid = (start + end) // 2
        if names[mid] == name:
            return mid
        if names[mid] > name:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search(names,"cat"))