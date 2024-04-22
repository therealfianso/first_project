with open("text_write.txt", "w") as file:
    print ("entre une ligne de texte (pour pour terminer tapez arrete ): ")
    while True :
        lign = input()
        if lign == "arrete" or lign == ".":
            break
        file.write(lign + "\n" )
print("les lignes a été enregistre.")
        