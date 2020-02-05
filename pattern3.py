r=int(input("enter the no. of rows"))
for i in range(0,r):
	for j in range(0,i):
		if i==0 or i==r-1:
			print("*"*4)
		else:
			print("*",end=" "*(r-2))
			print("*")
