n=int(input("enter the upper bound:"))
fib1=0
fib2=1
print(fib1)
print(fib2)
for i in range(2,n+1):
    fib3=fib2+fib1
    fib1=fib2
    fib2=fib3
    print(fib3)
