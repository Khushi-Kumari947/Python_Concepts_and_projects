while True:
    name=input("enter your name:")
    total=0
    while True:
        quantity=int(input("Enter the quantity of product purchased:"))
        amount=float(input("enter price of each product:"))
        total+=amount*quantity
        repeat=input("Have you purchased more products?")
        if(repeat=="no"):
            print("---------------------------------")
            break
    print("Printing your Bill:")
    print(name)
    print("Your total amount is:",total)
    print("*************Happy Shopping**************")
    repeat1=input("Next customer?")
    if(repeat1=="no"):
        break
