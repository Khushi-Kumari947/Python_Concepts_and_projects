#Program to find sum of all even numbers uoto 50

sum=0
for i in range(2,51):
    if(i%2==0):
        sum+=i
        # print(i)
print('Sum of all even numbers upto 50 is ',sum)