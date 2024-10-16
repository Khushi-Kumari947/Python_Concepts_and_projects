def calci(x,y,choice):
    if(choice==1):
        return x+y
    elif(choice==2):
        return(x-y)
    elif(choice==3):
        if(y!=0):
            return(x/y)
        else:
            return(print("Invalid divisio(cannot divide by zero)!!"))
    elif(choice==4):
        return (x*y)
    else:
        return(print("Not a valid choice"))
    

