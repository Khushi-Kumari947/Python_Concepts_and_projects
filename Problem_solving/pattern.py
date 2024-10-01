n=int(input("Enter any odd number:"))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("* * * * *","  ","* * * * *")

    if(i==(n+1)/2):
        print("* * * * * *")
    else:
        print("*         *")
        print("    *    ")
    print("\n")
