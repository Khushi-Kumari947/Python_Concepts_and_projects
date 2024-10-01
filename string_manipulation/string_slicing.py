print("****String slicing:****\n")

s="Happiness"

print("Including both start and end index")
substring=s[0:4]
print(substring,"\n")

print("Omitting any one last or first index")
print(s[:7])
print(s[4:],"\n")

print("Using negative indices")
print(s[-3:])
print(s[:-6],"\n")

print("Using step and (start,end,step) combination")
print(s[::2])
print("To reverse string s[::-1]",s[::-1])
print(s[0:10:3])
print("\n")