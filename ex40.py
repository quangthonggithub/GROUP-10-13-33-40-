a=float(input("enter the length of side 1:"))
b=float(input("enter the length of slide 2:"))
c=float(input("enter the length of slide 3:"))
if (a+b>c) and (a+c>b)and(b+c>a):
    if a==b==c:
         print("The triangle is an equilateral triangle")
    elif (a==b)or(b==c)or(c==a):
     print("The triangle is an isosceles triangle")
    else:
       print("The triangle is a scalene triangle")