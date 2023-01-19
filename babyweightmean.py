import math
babies = ["anna", "bob", "charlie"]
weights = [1500, 1620,1836]

avrage = math.fsum(weights)/len(weights)
print("\nThe avrage weight of the babies is", avrage)
print("\n")

for i in range(len(babies)):
    print(babies[i], "weighed", weights[i], "grams")
    print("This is", weights[i]-avrage, "grams away from the avrage weight\n")