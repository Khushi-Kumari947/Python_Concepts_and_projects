myset = {"apple", "banana", "cherry"}

#add():to add an element
myset.add("Guava")
print(myset)

#pop():to delete an item(random)
myset.pop()
print(myset)

#remove():to remove a particular element
myset.remove("cherry")
print(myset)

#Discard():to remove a particular element
myset.discard("Guava")
print(myset)

#copy()
b=myset.copy()
print(b)


x={"Ironman","Hulk","Captain America"}
y={"Superman","Batman","Wonder-Woman"}
z={"Hulk","Thor"}

#isdisjoint():
print(x.isdisjoint(y))

#issubset()
print(x.issubset(y))
print(z.issubset(x))

#issuperset
print(y.issuperset(x))
print(x.issuperset(z))

#update():to add one set to other
a=x.update(y)
print(a)

#clear():to empty set
a.clear()
print(a)

#union():Combines all elements from both sets, without duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  

# intersection ():Returns only elements present in both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set) 

# difference():Returns elements that are in the first set but not in the second.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)

# symmetric_difference():Returns elements that are in either of the sets but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

#difference_update():Removes elements from the set that are also in another set.
#This modifies the original set and doesn't return a new one
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1) 

#intersection_update():Keeps only elements that are present in both sets.
#This updates the original set to contain only the intersection

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

#symmetric_difference_update():Updates the set to keep elements that are in either set but not in both.
#Modifies the original set and removes elements that appear in both sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)