
numbers = input("Enter the numbers split with a space: ")
numbers = numbers.split()
print(numbers)
numbers = [float(i) for i in numbers]
avrage = sum(numbers)/len(numbers)
print(avrage)