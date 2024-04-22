s= str(input("donner un phrase : "))
#calculation combine caractere dans chaine
n = len(s)
#swap le le premier et le dernier caractere 
premier = s[0]
der= s[n-1]
c1=s[1:n-1]
c2=der + c1 + premier
#l'afficahge du resulata
print(c2)