datatosort = [3, 6, 8, 10, 1, 2, 1,42,15,57]

def Stalin_sort(array):
    max = array[0]
    new_array = [max]
    for i in array[1:]:
        if i >= max:
            max = i
            new_array.append(i)
    return new_array


    


print(Stalin_sort(datatosort))
