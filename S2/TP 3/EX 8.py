lignes_de_texte = ["hi my name is soufiane \n","and i made this script"]

with open("list_writelines.txt", "w") as file :
    file.writelines(lignes_de_texte)
print("the file is writen")