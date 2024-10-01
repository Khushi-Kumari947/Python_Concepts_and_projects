# 1
# 22
# 333
# 4444
# 55555
n=int(input("enter a number:"))
for i in range(1,n):
    for j in range (1,i+1):
        print(i,end=" ")
    print()

print("Next pattern!!")
# 654321
# 65432
# 6543
# 654
# 65
# 6

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()


print("Next pattern!!")
#     *
#    **
#   ***
#  ****
# *****

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()


print("Next pattern!!")
# 1
# 21
# 321
# 4321
# 54321

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

