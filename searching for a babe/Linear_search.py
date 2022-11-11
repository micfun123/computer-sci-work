
names=["cat","dog","mouses"]

def Linear_search_for(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def Linear_search_while(arr, key):
    i = 0
    while i < len(arr):
        if arr[i] == key:
            return i
        i += 1
    return -1

print(Linear_search_for(names,"cat"))
print(Linear_search_while(names,"cat"))