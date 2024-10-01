my_list = [[0] * 3] * 3
print(my_list)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

my_list[0][0] = 1
print(my_list)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]


funcs = [lambda x: x + i for i in range(5)]
print([f(10) for f in funcs])  # [14, 14, 14, 14, 14]



