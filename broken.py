raw = input("enter a number: ")

try: 
  int(raw)
except ValueError:
  print("error: enter a number")
else:
  print(f"the sum of the digits is: {sum([int(ch) for ch in raw])}")

for i in range(10):
    if i == int(raw):
        break
    print(i)
    

else:
   print("done")