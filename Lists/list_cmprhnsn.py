l1=[1,2,3,4,5,'e','g','Python',23]

l2=[]

for i in l1:
    l2.append(i)
print(l2)

l4=[20,45,62,35,12,80,76,43]
l3=[i for i in l4 if i>=45]
print(l3)