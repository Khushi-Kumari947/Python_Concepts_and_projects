#For loop is used when we have to perform a given set of statements multiple times
#range(a,b)-> a to b-1

n=int(input("Enter a number:"))
for i in range(1,n):
    print("Hello")

#Loop with gaps 
#for each specified jump starting from intial to last where each iteration is for initial +gap

print("The odd multipliers of", n ,"is from 1 to 50 is:")
for i in range(1,21,2):
    print(n,"X",i," = %2d ",n*i)