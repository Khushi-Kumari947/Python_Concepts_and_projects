#if_elif_else contionals are used when we have to choose from more than two options

Destn=input("Enter your destination:")

if(Destn=="delhi" or Destn== "Delhi" or Destn=="DELHI"):
    print("Your total fair would be 15k")
elif(Destn=="Kolakata" or Destn=="kolkata" or Destn=="KOLKATA"):
    print("Your total fair would be 25k")
else:
    print("No information about your destination")
print("Thank you")

x = 10
if (x == 10):
    print("X is exaclty 10")
elif(x<10):
    print("x is less than 10")
else:
    print("x is greater than 10")