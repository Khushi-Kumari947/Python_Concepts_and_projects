#Functions are set of code which are once crested can be used again and again in the program without writing code again

#defining a function

def hello():
    print("Hello!!")


hello()  #calling the function


#parameters:Written inside paratheseis at the function definition
#argumnets:Actual value passed to the function at function call

def add(x,y):
    print("sum of",x,"and",y,"is",x+y)

add(3,4)

#passing arbitrary arguments

def hii(*name):
    print("hello",name[2])

hii("Bella","Edward","Jacob")

#return statement

def hello():
    return "hello world"

print(hello())
