#Write a program to find maximum and minimum in a set
s={23,54,2,5,2,0,3}
print("The maximum number in set is",max(s))
print("The minimum number in set is",min(s))

#WAP to find common element in three lists using sets

a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]
print(set(a) & set(b) &set(c))

#WAP to find difference between two sets
s1={1,2,3,4,5}
s2={3,4,5}
print(s1.difference(s2)) #s1-s2

#WAP to remove an element from a set
s1={3,5,6,8,4,2}
s1.discard(6)
print(s1)

#   WAP to check if a set is subset of other set
s1={9,3,5,1,8,0}
s2={3,5,6}
print(s2.issubset(s1))  #s2(s1




