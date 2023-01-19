import math
babies = ["anna", "bob", "charlie","Michael"]
weights = [1500, 1620,1836,2700]

avrage = math.fsum(weights)/len(weights)
print("\nThe avrage weight of the babies is", avrage)
print("\n")

for i in range(len(babies)):
    #print(babies[i], "weighed", weights[i], "grams")
    #print("This is", weights[i]-avrage, "grams away from the avrage weight\n")
    if weights[i]-avrage > 500:
        print(babies[i], "weighed", weights[i], "grams")
        print("This is", weights[i]-avrage, "grams away from the avrage weight\n")
        print("This is more than 500 grams away from the avrage weight\n")