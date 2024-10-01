myString="Hello1209YOUh"

#isalnum():True if all characters in string are alphanumeric
print(myString,myString.isalnum())

myString="Hello"

#isalpha():True if all characters in string are in alphabet
print(myString,myString.isalpha())

myString="2341"

#isdecimal():True if all characters in string are in decimals
print(myString,myString.isdecimal())

myString="Hello 1209h"

#isnumeric():True if all characters in string are numeric
print(myString,myString.isnumeric())

myString="rainbow"

#islower():True if all characters in string are in lowercase
print(myString.islower())

myString="HELLOOO"

#isupper():True if all characters in string are in upper case
print(myString,myString.isupper())

myString="hii  "

#isspace():True if all characters in string are whitespaces
print(myString,myString.isspace())

myString="Hello World"

#istitle():True if all characters in string follows rules of title
print(myString,myString.istitle())

#endswith():Return true if string ends with the specified value
a="Harry Potter"
print(a.endswith("t",6,9))

#starswith():Returns true if string starts with the specified value
print(a.startswith("p",6,9))

#swapcase():lower case becomes upper case and vice-versa
print(a.swapcase())

#strip():Returns trimmed version of string
a="    Harry......Potter  *****"
print(a,a.strip(".,*, "))

#split():Splits the string at the specified separato and returns list
a="#OOFD#BRB#OMW#TB"
print(a.slpit("#"))

#ljust():Return a left justified versiojn of the string
a="Harry Potter"
a.ljust(4,"*")
print(a,"is a nice movie")

#rjust():Return a right justified versiojn of the string
a="Harry Potter"
a.rjust(5)
print(a,"is my favorite movie")

#replace():Returns a string where a specified valur=e is replaced with a value

a="My name is Bella"
print(a)
print(a.replace("Bella","Edward"))


