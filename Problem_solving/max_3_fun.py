#WAF to find maximum of 3 numbers

def maxi(x,y,z):
    if(x>y and x>z):
        return x
    elif(y>z):
        return y
    else:
        return z
    
print(maxi(12,9,75))