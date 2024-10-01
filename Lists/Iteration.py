list1=[80,"hello","Python",3,6,"is","Fun"]

print("Iteration using for loop")
#   Iteration using for loop
for i in list1:
    print(i)

#Iteration using for loop with length and range method
print("Iteration using for loop with length and range method")
for i in range(len(list1)):
    print(list1[i])

#Iteration using while loop
print("Iteration using while loop")
i=0
while(i<len(list1)):
    print(list1[i])
    i+=1

