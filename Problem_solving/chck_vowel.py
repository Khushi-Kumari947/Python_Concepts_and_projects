#program to check if passed character is vowel or consonant

ch=input("Enter a character:")

if (ch in "aeiou") or (ch in "AEIOU"):
    print("Passed character is a vowel")
else:
    print("Passed character is a consonant")
