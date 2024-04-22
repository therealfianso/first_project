s=str(input("donner le nom du fichier :"))
print(s)
#n = len(s)
l = s.split(".")
extension= "." + l[-1]
print("l'extension du fichier est : ", extension)