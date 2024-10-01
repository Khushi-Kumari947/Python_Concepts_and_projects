string=input("enter a string:")
char1=input("enter character to find occurence of:")
count=0
for i in string:
    if(i==char1):
        count+=1
print("The number occurence of ",char1,"in string",string,"is =",count)