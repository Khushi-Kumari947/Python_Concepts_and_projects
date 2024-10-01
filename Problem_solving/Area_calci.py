print("*****Area Calculation*****")
print("""Press 1:To calculate area of square
Press 2:To calculate area of rectangle
Press 3:To calculate area of circle
Press 4:To calculate area of triangle""")

choice=int(input())

if(choice==1):
    x=float(input("Enter side of square:"))
    print("Area of the square with side ",x," is:",x*x)
elif(choice==2):
    y=float(input("Enter length of rectangle:"))
    x=float(input("Enter breath of rectangle:"))
    print("Area of the rectangle with length ",y," and breath ",x," is:",y*x)
elif(choice==3):
    r=float(input("Enter the radius of circle :"))
    print("Area of the circle with radius ",r," is:",3.14*(r**2))
elif(choice==4):
    a=float(input("Enter the side of equilateral triangle:"))
    print("Area of equilateral triangle with side ",a," is:",0.43301*(a**2))
else:
    print("Invalid Choice!!")
