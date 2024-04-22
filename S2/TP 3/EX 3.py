file=open("exemple.txt", "r")
word = input("donner une mot-clé :")
content=file.readlines()
number= 0
for word in content :
    if word in content :
        number +=1
        print(f"le mot a {word} ete trouve {number} fois ")
    else : 
        print(f"le mot {word} ne pas dans le fichier")

file.close