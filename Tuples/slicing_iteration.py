tupl=("OnePLus","Vivo","SamSung","Redmi","Nokia")

#Slicing in tuples
print(tupl[1:3])
print(tupl[:3])
print(tupl[::2])
print(tupl[::-1])


#Iteration i tuples

for i in tupl:   #just using for loop
    print(i)

for i in range(len(tupl)):  #for loop wiht range and len
    print(tupl[i])


i=0
while(i<len(tupl)):   #using while loop
    print(tupl[i])
    i+=1


