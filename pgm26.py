mylist=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
	x=int(input("enter the numbers"))
	mylist.insert(x)
print(min(mylist))
print(mylist)

