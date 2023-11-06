staff = ["anna", "bob", "charlie"]
sales = [[100, 110, 120, 110], [200, 210, 220, 210], [300, 310, 320, 310]]

total = 0

print("Lets see how much each staff member sold")
for i in range(len(staff)):
    print(staff[i], "sold", sum(sales[i]), "in total")
    for j in range(len(sales[i])):
        print("On Quarter", j + 1, "they sold", sales[i][j])
    print("\n")
    total += sum(sales[i])
print("Total sales:", total)
