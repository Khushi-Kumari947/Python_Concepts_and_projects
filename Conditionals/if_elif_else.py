#if_elif_else contionals are used when we have to choose from more than two options

Destn=input("Enter your destination:")

if(Destn=="delhi" or Destn== "Delhi" or Destn=="DELHI"):
    print("Your total fair would be 15k")
elif(Destn=="Kolakata" or Destn=="kolkata" or Destn=="KOLKATA"):
    print("Your total fair would be 25k")
else:
    print("No information about your destination")
print("Thank you")