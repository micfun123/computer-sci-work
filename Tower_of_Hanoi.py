

def solver(number_of_disks, start, end, temp):
    if number_of_disks == 1:
        print("Move disk 1 from rod", start, "to rod", end)
        return
    solver(number_of_disks - 1, start, temp, end)
    print("Move disk", number_of_disks, "from rod", start, "to rod", end)
    solver(number_of_disks - 1, temp, end, start)

solver(3, "A", "C", "B")