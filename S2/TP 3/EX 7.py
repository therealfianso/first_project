with open("ligne_writeline.txt", "w") as file :
    ligne= input("ecrire une seule ligne de texte : ")
    file.writelines(ligne)
