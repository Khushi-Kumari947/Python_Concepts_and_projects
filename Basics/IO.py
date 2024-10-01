name='John'
id=2
address="645 lake street"

print(name,"\n",id,"\n",address)

#To know the type of any variable we use type()

print(type(name))
print(type(id))
print(type(address))

#explicit conversion

f=float(input("enter any floating point number:"))
print("Number is ",f,"having type:",type(f))
f=int(f)
print("Number is ",f,"after explicit coversion having type:",type(f))