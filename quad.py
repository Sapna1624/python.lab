from math import sqrt
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=b**2-4*a*c
if d>0:
	x1=(-b+sqrt(d))/(2*a)
	print("Positive root",x1)
	x2=(-b-sqrt(d))/(2*a)
	print("Negative root",x2)
else:
	print("roots are imaginary")
