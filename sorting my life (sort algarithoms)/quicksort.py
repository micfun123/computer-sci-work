datatosort = [3, 6, 8, 10, 1, 2, 1,42,2,15,57]

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort(datatosort))
