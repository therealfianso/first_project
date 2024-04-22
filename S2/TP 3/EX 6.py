import random

random_numbers = [random.randint(1, 100, 2) for _ in range(10)]

with open("nombres_writelines.txt", "w") as file:
     
    mylist = []
    n = len(mylist)
    for number in random_numbers : 
        mylist.append(str(number) + "\n")
    file.writelines(mylist)

