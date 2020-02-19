t=tuple(map(eval,input("enter:: ").split()))
b=[]
for i in t:
	if t.count(i)>1 and i not in b:
		print(i)
		b.append(i)
