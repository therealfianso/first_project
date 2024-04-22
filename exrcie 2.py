s = str(input("donner un phrase :"))
# regrouper les caractères de s dans un ensemble pour éviter les répetitions
unique =set({})
#print(unique)
for x in s:
    if x not in unique:
        unique.add(x)
        print("Le nombre d'occurrences du caractère: ", x, " dans la chaine s est :", s.count(x))