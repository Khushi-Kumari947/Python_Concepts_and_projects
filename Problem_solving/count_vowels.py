Mystr=input("Enter a string:")
count=0
for i in Mystr:
    if(i in ("AEIOUaeiou")):
        count+=1
print("The number of vowels in given string is =",count)
