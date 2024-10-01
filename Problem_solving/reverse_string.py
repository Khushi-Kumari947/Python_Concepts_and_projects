Mystr=input('Enter a string:')
# print(Mystr[::-1])
n=len(Mystr)
rev=""
for i in Mystr:
    rev=i+rev
print(rev)


if(Mystr==rev):
    print("Given string is a palindrome!")
else:
    print("Not a palindrome!")


    

 