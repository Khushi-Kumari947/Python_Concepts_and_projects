n=int(input("enter a number:"))
a=n
rev=0
digit=0
while(a!=0):
    digit=a%10
    rev=rev*10+digit
    a=a//10
    print(rev)
if(n==rev):
    print("Given number is a plaindrome!")
else:
    print("Not a palindrome!")