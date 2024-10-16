#local variable:Restricted to only one block and cannot be changed or accessed in whole program
# global:not restricted to single block and can be used and accessed throughout the program

#Local variable

x=30

def fun1():
    x=23
    return x

print("value of x before fun1 call",x)
r=fun1()
print("value of x after fun1 call",x)

#Global variable

c=45

def fun2():
    global c
    c=10
    return c

print("value of c before fun2 call",c)
s=fun2()
print("value of c after fun2 call",c)
