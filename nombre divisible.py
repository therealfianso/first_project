def nombreDivisibles(L,n):
    div = 0
    for k in L:
        if (k%n == 0):
            div = div + 1
    return div
L=[5,9,3,5,6,7,87,4]
n=3
print("Le nombre d'élément de L qui sont divisible par " , n , " est : " ,nombreDivisibles(L,n))