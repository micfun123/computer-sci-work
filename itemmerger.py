def remove_dupe(inputelist):
    return list(dict.fromkeys(inputelist))

list_one = ["cat","dog","panda","camel","pig"]
list_two = ["cat","dog","panda","camel","pig","apple","cake"]

list_one = list_one + list_two
list_one = remove_dupe(list_one)

print(list_one)
