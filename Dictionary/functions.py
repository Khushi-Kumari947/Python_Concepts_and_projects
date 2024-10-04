thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#get():to value of any key
print(thisdict.get("brand"))

#items():To get all key values pair
print(thisdict.items())

#keys:To get all keys
print(thisdict.keys())

#values:To get all values
print(thisdict.values())

#copy():to copy our dictionary

d=thisdict.copy()
print(d)

#Nested dictionary
employ={1:{"name":"John","age":23,"gender":"male"},
        2:{"name":"Lisa","age":24,"gender":"female"},
        3:{"name":"Peter","age":22,"gender":"male"}}

print(employ[1])