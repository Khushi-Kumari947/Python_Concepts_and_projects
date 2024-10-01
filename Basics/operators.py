#Arithmetic operators
print("Arithmetic operators:\n")
x=34
y=7
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Normal divison:",x/y) #Normal division returns quotient
print("Floor division:",x//y)#Floor division return integral part of quotient
print("Modulus operator:",x%y) #return remainder
print("exponentiation 2**4:",2**4) #return remainder
print("\n")

#Comparison operators
print("Comparison operators:\n")
a=19
b=5
print("a =",a,"b =",b)
print("a>b:",a>b)
print("a<b:",a<b)
print("a==b:",a==b)
print("a!=b:",a!=b)
print("a<=b:",a<=b)
print("a>=b:",a>=b)
print("\n")

#logical operators
print("logical operators:\n")
a=19
b=5
print("a =",a,"b =",b)
print("a==b and a>b:",a==b and a>b)
print("a==b or a>b:",a==b or a>b)
print("not a<=b:",not(a<=b))
print("\n")

#Assignment operators
print("Assignment operators:\n")
a=19
print("a =",a)
a+=1
print("a+=1",a)
a-=5
print("a-=5",a)
a*=3
print("a*=3",a)
print("\n")

#Identity operators

print("Identity Operators\n")
u="123"
v=123
print("u is v:",u is v)
print("u is not v:",u is not v)
print("\n")

#Bitwise operators
u=10
v=5
print("Bitwise Operators\n")
print(" u:",bin(u)," v:",bin(v))
print("u&v:",u&v)
print("u|v:",u|v)
print("u^v:",u^v)
print("u<<1:",u<<1)
print("u>>1:",u>>1)
print("\n")

#Membership Operators
print("Membership Operators\n")
u="hello"
print("'P' in 'hello':",'p' in u)
print("'P' not in 'hello':",'p' not in u)
print("\n")
