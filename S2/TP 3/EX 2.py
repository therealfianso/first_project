file=open("exemple.txt", "r")
content=file.readlines()
number= 0
for i in content :
    number +=1
print(number)
file.close