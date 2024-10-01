sname="Hello world"

#len():To find length of given string
print("The length of",sname,"is =",len(sname))

#count():To return the frequency of any character in a string
print("The frequency of 'o' in",sname,"is =",sname.count("o"))

#upper():To make all element of string capital
print("The upper case of",sname,"is =",sname.upper())

#lower():To make all element of string lower case
print("The lower case of",sname,"is =",sname.upper())

#index():to find index of given char in string
print("The index of w in",sname,"is =",sname.index("w"))

#lower():To make first letter of string upper case
print("Capatalize string is =",sname.capitalize())

#find():To find index of given element
print("Index of l is",sname.find("l"))

#format():To do formatting in the string
name="India"
str1="I love my {}"
print("str1.format(name):",str1.format(name))

#center(total_number_of_char,[specific character]):To make alignment of string to the center
name="Khushi"
print(name.center(15,"✨"))


